from __future__ import annotations

from datetime import date
from pathlib import Path
import re

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[2]
SOURCE_PDF = ROOT / "MW5Mercs_Mod_Editor_Guide_(v2.3).pdf"
OUTPUT_MD = (
    ROOT
    / "reports"
    / "tku_editor_first"
    / "mw5_mod_editor_guide_v2_3_reference.md"
)

ASCII_REPLACEMENTS = {
    "\u2018": "'",
    "\u2019": "'",
    "\u201a": "'",
    "\u201c": '"',
    "\u201d": '"',
    "\u201e": '"',
    "\u2013": "-",
    "\u2014": "-",
    "\u2212": "-",
    "\u2022": "-",
    "\u2026": "...",
    "\u00a0": " ",
    "\u00ae": "(R)",
    "\u2122": "(TM)",
}

SECTION_TITLES = {
    "Mod Editor Guide Changelog",
    "Introduction",
    "Initial Launch",
    "Making a Mod",
    "Create Mod",
    "Creating a Substitution Mod",
    "Creating a New Asset Mod",
    "Manage Mod",
    "Installing your new Mod to the game",
    "Porting your existing Mod into the new Mod framework (Recommended approach)",
    "Porting your existing Mod into the new Mod framework (Basic approach)",
    "Compatibility of Mods made in v1 of the Mod Editor",
    "Changing the Load Order of a Mod after it has been packaged",
    "Using Custom Data Tables",
    "Using Custom Tag Containers",
    "Including External Assets with your Mod",
    "Adding New Input Events",
    "Using the Mod Editor",
    "Creating a basic Test Map",
    "Spawning an AI 'Mech",
    "Spawning as a 'Mech",
    "Creating a new Weapon",
    "Modifying a 'Mech Loadout asset",
    "Using Audiokinetic Wwise to Mod music and sound in MW5",
    "Registering your Wwise Project",
    "Installing Wwise",
    "Getting Started",
    "Adding your Non-Commercial License",
    "Importing your sound file into the MW5 Wwise Project",
    "Setting up the Editor with Wwise",
    "Important steps before packaging your Audio Mod",
}

BEST_PRACTICES = """\
## Quick Best-Practices Reference

### Project Safety

- Install the Mod Editor on an SSD if possible.
- Use version control or a reliable backup system before serious mod work.
- Let "Discovering Asset Data" and "Loading MechWarrior Assets" fully complete before editing.
- Treat this workspace as a staging/reference workspace, not the live game install.
- Do not overwrite original TKU paks or loose required override paks in place.

### Mod Setup

- Start every project by creating a mod package with the Create Mod interface.
- Keep the correct mod selected in Active Mod before creating or saving assets.
- Add an author and description even though only the mod name is required.
- Use Manage Mod only after the mod has the content you intend to package.

### Asset Organization

- Put modified copies of existing game content in ModOverride Content.
- Put new, non-substitution assets in <ModName> Content.
- For ported ModOverride assets, preserve the exact folder structure of the original asset.
- Use Save To Mod on existing game assets instead of editing source game assets directly.
- Use Open Game Asset only as a reference path back to the original asset.

### Substitution Mods

- Create or select the mod, then open the original game asset.
- Click Save To Mod to create the safe override copy.
- Make changes only inside the modded asset.
- When changing a weapon data asset directly, disable table-driven overwrite behavior where the guide calls for it.

### New Assets

- Create new assets in the mod content folder.
- If an existing system must use the new asset, create a substitution mod for the referencing asset and point it at the new asset.
- Keep related new assets and their referencing overrides together in the same active mod.

### Packaging And Installation

- Set a clear version number before packaging.
- Leave load order at the default unless the mod deliberately depends on another mod's behavior.
- Package through Manage Mod and test the packaged output, not just the editor state.
- Copy the packaged mod folder into the game's MW5Mercs/Mods folder, enable it from the in-game Mods screen, apply, and restart the game.
- For old v1-style pak-only mods, the game can still read paks from MW5Mercs/Content/Paks, but they will not appear in the in-game Mods screen unless ported.

### Data Tables, Tags, Inputs, And External Files

- Prefer custom data tables for weapon mods so multiple weapon mods do not all depend on the same default stats table.
- Copy custom data tables into <ModName> Content rather than ModOverride Content.
- Export copied data tables as JSON when the guide calls for an external source file.
- Put gameplay tag config under Plugins/<ModName>/Config.
- Put Wwise audio output under Plugins/<ModName>/ModOverride/WwiseAudio.
- Put custom input events in Plugins/<ModName>/Config/Input/<ModName>Input.ini.
- The editor can refresh newly saved input event config without a full editor restart.

### Testing In The Editor

- Build a basic test map with a large floor, lighting, player start, sky sphere, skylight, fog, and reflection capture.
- Use SpawnPoint actors for AI 'Mechs and configure spawn-on-begin-play behavior when useful.
- Use TestMode to spawn as a selected 'Mech loadout.
- Save To Mod before changing existing 'Mech loadout assets.
- Test the modded loadout or weapon in editor play mode before packaging.

### Wwise Audio Mods

- Use Wwise Authoring 2021.1.2.7629 for the guide's v2.3 workflow.
- Register the project using the required "MW5Mercs Modding (...)" project naming pattern.
- Do not click "Integrate Wwise into Project"; open the MW5 Wwise project instead.
- Regenerate the relevant SoundBank after replacing audio.
- A SoundBank generation failure can be expected when source audio is missing for unrelated assets; verify that the changed event was generated and refreshed.
- Before packaging an audio mod, make sure required external WwiseAudio files are in the mod's ModOverride/WwiseAudio path.

### TKU Update Workflow Notes

- Keep editor-first evidence and generated references under reports/tku_editor_first.
- Use Mod Editor behavior as the primary compatibility signal; treat UAssetAPI, FModel, umodel, Blender, UAssetGUI, and UE4SS findings as supporting evidence.
- For TKU repair work, prefer a small editor-authored override or plugin-only change over touching live original assets.
"""

QUICK_LOOKUP = """\
## Quick Lookup

Search these headings in this file:

- Create Mod
- Creating a Substitution Mod
- Creating a New Asset Mod
- Manage Mod
- Installing your new Mod to the game
- Porting your existing Mod into the new Mod framework
- Changing the Load Order of a Mod after it has been packaged
- Using Custom Data Tables
- Using Custom Tag Containers
- Including External Assets with your Mod
- Adding New Input Events
- Creating a basic Test Map
- Spawning an AI 'Mech
- Spawning as a 'Mech
- Creating a new Weapon
- Modifying a 'Mech Loadout asset
- Using Audiokinetic Wwise to Mod music and sound in MW5
- Important steps before packaging your Audio Mod
"""


def ascii_clean(text: str) -> str:
    for old, new in ASCII_REPLACEMENTS.items():
        text = text.replace(old, new)
    return text.encode("ascii", errors="ignore").decode("ascii")


def clean_line(line: str) -> str:
    line = ascii_clean(line)
    line = re.sub(r"\.{4,}", " ", line)
    line = re.sub(r"[ \t]+", " ", line)
    return line.strip()


def format_page_text(text: str) -> str:
    formatted: list[str] = []
    previous_blank = True

    for raw_line in text.splitlines():
        line = clean_line(raw_line)
        if not line:
            if not previous_blank:
                formatted.append("")
            previous_blank = True
            continue

        if line in SECTION_TITLES:
            if formatted and formatted[-1] != "":
                formatted.append("")
            formatted.append(f"## {line}")
            formatted.append("")
            previous_blank = True
            continue

        if line.startswith("-"):
            formatted.append(line)
        else:
            formatted.append(line)
        previous_blank = False

    while formatted and formatted[-1] == "":
        formatted.pop()

    return "\n".join(formatted)


def build_reference() -> str:
    reader = PdfReader(str(SOURCE_PDF))
    metadata = reader.metadata or {}
    title = "MW5 Mercs Mod Editor Guide v2.3 Reference"
    author = ascii_clean(str(metadata.get("/Author", "unknown")))
    producer = ascii_clean(str(metadata.get("/Producer", "unknown")))
    parts: list[str] = [
        f"# {title}",
        "",
        f"Source PDF: `{SOURCE_PDF.name}`",
        f"Generated: {date.today().isoformat()}",
        f"Pages extracted: {len(reader.pages)}",
        f"PDF author: {author}",
        f"PDF producer: {producer}",
        "",
        "This file is a searchable working reference derived from the PDF text extraction. "
        "Screenshots and visual callouts from the source PDF are not reproduced, so use the "
        "PDF when you need exact UI placement.",
        "",
        BEST_PRACTICES.strip(),
        "",
        QUICK_LOOKUP.strip(),
        "",
        "# Extracted Guide Text",
        "",
    ]

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        parts.append(f"## PDF Page {page_number:02d}")
        parts.append("")
        parts.append(format_page_text(text))
        parts.append("")

    return "\n".join(parts).strip() + "\n"


def main() -> None:
    if not SOURCE_PDF.exists():
        raise FileNotFoundError(SOURCE_PDF)

    OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_MD.write_text(build_reference(), encoding="utf-8", newline="\n")
    print(OUTPUT_MD)


if __name__ == "__main__":
    main()
