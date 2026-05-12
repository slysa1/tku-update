from __future__ import annotations

import hashlib
import struct
from dataclasses import dataclass
from pathlib import Path

PAK_MAGIC = 0x5A6F12E1
UE_ASSET_MAGIC = 0x9E2A83C1
FOOTER_SZ_V11 = 221
FOOTER_SZ_LEGACY = 45
PF_HEADER_SZ = 53

SIDECAREXT = {".uasset", ".uexp", ".ubulk", ".umap"}


def _u8(data: bytes, pos: int) -> tuple[int, int]:
    return struct.unpack_from("B", data, pos)[0], pos + 1


def _u32(data: bytes, pos: int) -> tuple[int, int]:
    return struct.unpack_from("<I", data, pos)[0], pos + 4


def _i32(data: bytes, pos: int) -> tuple[int, int]:
    return struct.unpack_from("<i", data, pos)[0], pos + 4


def _i64(data: bytes, pos: int) -> tuple[int, int]:
    return struct.unpack_from("<q", data, pos)[0], pos + 8


def _u64(data: bytes, pos: int) -> tuple[int, int]:
    return struct.unpack_from("<Q", data, pos)[0], pos + 8


def _fstr(data: bytes, pos: int) -> tuple[str, int]:
    length, pos = _i32(data, pos)
    if length == 0:
        return "", pos
    if length > 0:
        raw = data[pos : pos + length]
        return raw.rstrip(b"\x00").decode("utf-8", "replace"), pos + length
    num_bytes = -length * 2
    raw = data[pos : pos + num_bytes]
    return raw.rstrip(b"\x00\x00").decode("utf-16-le", "replace"), pos + num_bytes


@dataclass(frozen=True)
class PakFooter:
    version: int
    index_offset: int
    index_size: int
    encrypted_index: bool
    compression_methods: tuple[str, ...]


@dataclass(frozen=True)
class PakEntry:
    pak_path: str
    game_path: str
    extension: str
    encoded_offset: int
    offset: int
    size: int
    uncompressed_size: int
    compression_method_index: int
    encrypted: bool

    @property
    def base_game_path(self) -> str:
        return self.game_path[: -len(self.extension)]


def read_footer(handle) -> PakFooter:
    handle.seek(0, 2)
    file_size = handle.tell()
    if file_size >= FOOTER_SZ_V11:
        handle.seek(file_size - FOOTER_SZ_V11)
        footer = handle.read(FOOTER_SZ_V11)
        pos = 16
        encrypted_index_raw, pos = _u8(footer, pos)
        magic, pos = _u32(footer, pos)
        if magic == PAK_MAGIC:
            version, pos = _i32(footer, pos)
            index_offset, pos = _i64(footer, pos)
            index_size, pos = _i64(footer, pos)
            pos += 20
            methods: list[str] = []
            if version >= 8:
                for _ in range(5):
                    methods.append(footer[pos : pos + 32].rstrip(b"\x00").decode("ascii", "replace"))
                    pos += 32
            return PakFooter(
                version=version,
                index_offset=index_offset,
                index_size=index_size,
                encrypted_index=bool(encrypted_index_raw),
                compression_methods=tuple(methods),
            )

    if file_size >= FOOTER_SZ_LEGACY:
        handle.seek(file_size - FOOTER_SZ_LEGACY)
        footer = handle.read(FOOTER_SZ_LEGACY)
        pos = 0
        encrypted_index_raw, pos = _u8(footer, pos)
        magic, pos = _u32(footer, pos)
        if magic == PAK_MAGIC:
            version, pos = _i32(footer, pos)
            index_offset, pos = _i64(footer, pos)
            index_size, pos = _i64(footer, pos)
            return PakFooter(
                version=version,
                index_offset=index_offset,
                index_size=index_size,
                encrypted_index=bool(encrypted_index_raw),
                compression_methods=tuple(),
            )

    raise ValueError("not a supported pak file")


def read_main_index(handle, footer: PakFooter) -> tuple[str, int, int, bytes]:
    handle.seek(footer.index_offset)
    data = handle.read(footer.index_size)
    if footer.version < 8:
        mount_point, _ = _fstr(data, 0)
        return mount_point, 0, 0, data
    pos = 0
    mount_point, pos = _fstr(data, pos)
    _, pos = _i32(data, pos)
    _, pos = _u64(data, pos)
    has_phi, pos = _i32(data, pos)
    if has_phi:
        pos += 8 + 8 + 20
    has_fdi, pos = _i32(data, pos)
    fdi_offset = 0
    fdi_size = 0
    if has_fdi:
        fdi_offset, pos = _i64(data, pos)
        fdi_size, pos = _i64(data, pos)
        pos += 20
    encoded_len, pos = _i32(data, pos)
    encoded = data[pos : pos + encoded_len]
    return mount_point, fdi_offset, fdi_size, encoded


def read_fdi(handle, fdi_offset: int, fdi_size: int) -> dict[str, dict[str, int]]:
    handle.seek(fdi_offset)
    data = handle.read(fdi_size)
    pos = 0
    num_dirs, pos = _i32(data, pos)
    directory_map: dict[str, dict[str, int]] = {}
    for _ in range(num_dirs):
        dir_name, pos = _fstr(data, pos)
        num_files, pos = _i32(data, pos)
        file_map: dict[str, int] = {}
        for _ in range(num_files):
            filename, pos = _fstr(data, pos)
            encoded_offset, pos = _u32(data, pos)
            file_map[filename] = encoded_offset
        directory_map[dir_name] = file_map
    return directory_map


def decode_entry(encoded: bytes, pos: int) -> tuple[dict[str, int | bool], int]:
    flags, pos = _u32(encoded, pos)
    num_blocks = (flags >> 6) & 0xFFFF
    encrypted = bool((flags >> 22) & 1)
    compression_method_index = (flags >> 23) & 0x3F
    size_is_32 = bool((flags >> 29) & 1)
    uncompressed_is_32 = bool((flags >> 30) & 1)
    offset_is_32 = bool((flags >> 31) & 1)
    if offset_is_32:
        offset, pos = _u32(encoded, pos)
    else:
        offset, pos = _u64(encoded, pos)
    if uncompressed_is_32:
        uncompressed_size, pos = _u32(encoded, pos)
    else:
        uncompressed_size, pos = _u64(encoded, pos)
    if compression_method_index:
        if size_is_32:
            size, pos = _u32(encoded, pos)
        else:
            size, pos = _u64(encoded, pos)
    else:
        size = uncompressed_size
    pos += num_blocks * 16
    return {
        "offset": offset,
        "size": size,
        "uncompressed_size": uncompressed_size,
        "compression_method_index": compression_method_index,
        "encrypted": encrypted,
    }, pos


def resolve_data_offset(handle, raw_offset: int) -> int:
    handle.seek(raw_offset)
    probe = handle.read(8)
    if len(probe) < 8:
        return raw_offset
    if struct.unpack("<I", probe[:4])[0] == UE_ASSET_MAGIC:
        return raw_offset
    if probe != b"\x00" * 8:
        return raw_offset
    return raw_offset + PF_HEADER_SZ


def normalise_game_path(dir_path: str, filename: str, mount_point: str = "") -> str:
    combined = (dir_path + filename).replace("\\", "/")
    for marker in ("/Game/", "Game/", "/Plugins/", "Plugins/"):
        idx = combined.find(marker)
        if idx != -1:
            if marker.startswith("/"):
                return combined[idx:]
            return "/" + combined[idx:]
    for marker in ("/Content/", "Content/"):
        idx = combined.find(marker)
        if idx != -1:
            start = idx + (1 if marker.startswith("/") else 0)
            content_path = combined[start:]
            return "/Game/" + content_path[len("Content/") :]
    if mount_point.replace("\\", "/").rstrip("/").endswith("/Content"):
        return "/Game/" + combined.strip("/")
    if combined.startswith("Content/"):
        return "/Game/" + combined[len("Content/") :]
    return "/" + combined.strip("/")


def iter_entries(pak_path: Path) -> tuple[PakFooter, str, list[PakEntry]]:
    with pak_path.open("rb") as handle:
        footer = read_footer(handle)
        if footer.encrypted_index:
            raise ValueError(f"encrypted pak index not supported: {pak_path}")
        mount_point, fdi_offset, fdi_size, encoded = read_main_index(handle, footer)
        if footer.version < 8:
            pos = 0
            mount_point, pos = _fstr(encoded, pos)
            num_entries, pos = _i32(encoded, pos)
            entries: list[PakEntry] = []
            for _ in range(num_entries):
                filename, pos = _fstr(encoded, pos)
                offset, pos = _i64(encoded, pos)
                size, pos = _i64(encoded, pos)
                uncompressed_size, pos = _i64(encoded, pos)
                compression_method_index, pos = _i32(encoded, pos)
                pos += 20
                encrypted_raw, pos = _u8(encoded, pos)
                _, pos = _u32(encoded, pos)
                game_path = normalise_game_path(mount_point, filename, mount_point)
                entries.append(
                    PakEntry(
                        pak_path=(mount_point + filename).replace("\\", "/"),
                        game_path=game_path,
                        extension=Path(filename).suffix.lower(),
                        encoded_offset=-1,
                        offset=offset,
                        size=size,
                        uncompressed_size=uncompressed_size,
                        compression_method_index=compression_method_index,
                        encrypted=bool(encrypted_raw),
                    )
                )
            entries.sort(key=lambda item: item.game_path.lower())
            return footer, mount_point, entries
        if not fdi_offset:
            raise ValueError(f"full directory index missing: {pak_path}")
        directory_map = read_fdi(handle, fdi_offset, fdi_size)
        entries: list[PakEntry] = []
        for dir_path, file_map in directory_map.items():
            for filename, encoded_offset in file_map.items():
                entry, _ = decode_entry(encoded, encoded_offset)
                game_path = normalise_game_path(dir_path, filename, mount_point)
                entries.append(
                    PakEntry(
                        pak_path=(dir_path + filename).replace("\\", "/"),
                        game_path=game_path,
                        extension=Path(filename).suffix.lower(),
                        encoded_offset=encoded_offset,
                        offset=int(entry["offset"]),
                        size=int(entry["size"]),
                        uncompressed_size=int(entry["uncompressed_size"]),
                        compression_method_index=int(entry["compression_method_index"]),
                        encrypted=bool(entry["encrypted"]),
                    )
                )
        entries.sort(key=lambda item: item.game_path.lower())
        return footer, mount_point, entries


def extract_exact_paths(pak_path: Path, wanted_paths: set[str]) -> dict[str, bytes]:
    wanted_lower = {path.lower(): path for path in wanted_paths}
    extracted: dict[str, bytes] = {}
    footer, _, entries = iter_entries(pak_path)
    if footer.encrypted_index:
        raise ValueError(f"encrypted pak index not supported: {pak_path}")
    with pak_path.open("rb") as handle:
        for pak_entry in entries:
            wanted_path = wanted_lower.get(pak_entry.game_path.lower())
            if not wanted_path:
                continue
            if pak_entry.encrypted or pak_entry.compression_method_index != 0:
                raise ValueError(f"cannot extract compressed or encrypted entry: {pak_entry.game_path}")
            data_offset = resolve_data_offset(handle, pak_entry.offset)
            handle.seek(data_offset)
            extracted[wanted_path] = handle.read(pak_entry.size)
    return extracted


def gather_sidecar_paths(entries: list[PakEntry], base_paths: set[str]) -> list[str]:
    base_lookup = {base.lower() for base in base_paths}
    wanted: list[str] = []
    for pak_entry in entries:
        if pak_entry.extension not in SIDECAREXT:
            continue
        if pak_entry.base_game_path.lower() in base_lookup:
            wanted.append(pak_entry.game_path)
    return wanted


def game_path_to_pak_path(game_path: str) -> str:
    stripped = game_path.lstrip("/")
    if stripped.startswith("Game/"):
        return "Content/" + stripped[len("Game/") :]
    return stripped


def collect_loose_files(content_root: Path) -> list[tuple[str, bytes]]:
    files: list[tuple[str, bytes]] = []
    for path in sorted(content_root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(content_root).as_posix()
        files.append(("/Game/" + rel, path.read_bytes()))
    return files


def sha1(data: bytes) -> bytes:
    return hashlib.sha1(data).digest()


def _write_fstring(text: str) -> bytes:
    raw = (text + "\x00").encode("utf-8")
    return struct.pack("<i", len(raw)) + raw


def encode_entry(offset: int, size: int, uncompressed_size: int) -> bytes:
    offset_is_32 = offset < 0x1_0000_0000
    size_is_32 = size < 0x1_0000_0000
    uncompressed_is_32 = uncompressed_size < 0x1_0000_0000
    flags = 0
    flags |= int(size_is_32) << 29
    flags |= int(uncompressed_is_32) << 30
    flags |= int(offset_is_32) << 31
    encoded = bytearray(struct.pack("<I", flags))
    encoded += struct.pack("<I" if offset_is_32 else "<Q", offset)
    encoded += struct.pack("<I" if uncompressed_is_32 else "<Q", uncompressed_size)
    return bytes(encoded)


def build_pak(files: list[tuple[str, bytes]], output_path: Path, mount_point: str = "../../../MW5Mercs/") -> int:
    files = sorted(files, key=lambda item: item[0].lower())
    data_buf = bytearray()
    entry_info: list[tuple[str, int, int, bytes]] = []
    for game_path, payload in files:
        offset = len(data_buf)
        data_buf += payload
        entry_info.append((game_path, offset, len(payload), sha1(payload)))

    encoded_buf = bytearray()
    entry_byte_offsets: list[int] = []
    for game_path, offset, size, _ in entry_info:
        _ = game_path
        entry_byte_offsets.append(len(encoded_buf))
        encoded_buf += encode_entry(offset, size, size)

    dir_map: dict[str, dict[str, int]] = {}
    for index, (game_path, _, _, _) in enumerate(entry_info):
        pak_path = game_path_to_pak_path(game_path)
        path_obj = Path(pak_path)
        dir_name = path_obj.parent.as_posix() + "/"
        dir_map.setdefault(dir_name, {})[path_obj.name] = entry_byte_offsets[index]

    fdi = bytearray(struct.pack("<i", len(dir_map)))
    for dir_name, file_map in dir_map.items():
        fdi += _write_fstring(dir_name)
        fdi += struct.pack("<i", len(file_map))
        for filename, encoded_offset in file_map.items():
            fdi += _write_fstring(filename)
            fdi += struct.pack("<I", encoded_offset)
    fdi_bytes = bytes(fdi)

    def make_index(fdi_offset: int) -> bytes:
        index = bytearray()
        index += _write_fstring(mount_point)
        index += struct.pack("<i", 0)
        index += struct.pack("<Q", 0)
        index += struct.pack("<i", 0)
        index += struct.pack("<i", 1)
        index += struct.pack("<q", fdi_offset)
        index += struct.pack("<q", len(fdi_bytes))
        index += sha1(fdi_bytes)
        index += struct.pack("<i", len(encoded_buf))
        index += encoded_buf
        index += struct.pack("<i", 0)
        return bytes(index)

    data_size = len(data_buf)
    index_bytes = make_index(0)
    final_fdi_offset = data_size + len(index_bytes)
    index_bytes = make_index(final_fdi_offset)

    footer = bytearray()
    footer += b"\x00" * 16
    footer += struct.pack("B", 0)
    footer += struct.pack("<I", PAK_MAGIC)
    footer += struct.pack("<i", 11)
    footer += struct.pack("<q", data_size)
    footer += struct.pack("<q", len(index_bytes))
    footer += sha1(index_bytes)
    for _ in range(5):
        footer += b"\x00" * 32

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("wb") as handle:
        handle.write(data_buf)
        handle.write(index_bytes)
        handle.write(fdi_bytes)
        handle.write(footer)

    return len(data_buf) + len(index_bytes) + len(fdi_bytes) + len(footer)
