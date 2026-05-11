from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TierRule:
    prefix: str
    domain: str
    patch_tier: str
    proposed_action: str


PATCH_NAME = "TheKnownUniverseCompatPatch"
PATCH_DISPLAY_NAME = "The Known Universe Compatibility Patch"
PATCH_VERSION = "0.3.0"
PATCH_BUILD_NUMBER = 3
PATCH_LOAD_ORDER = 999
PATCH_GAME_VERSION = "1.13.378"
TIER_ORDER = ("A", "B", "C")

TIER_RULES: tuple[TierRule, ...] = (
    TierRule("/Game/Levels/FrontEnd/StarMap", "frontend_starmap_level", "A", "replace_with_vanilla"),
    TierRule("/Game/UI/FrontEnd/StarMapPawn", "frontend_starmap_pawn", "A", "replace_with_vanilla"),
    TierRule("/Game/UI/FrontEnd/Starmap/StarMapActor", "frontend_starmap_actor", "A", "replace_with_vanilla"),
    TierRule("/Game/UI/FrontEnd/Starmap/StarSystemBody", "frontend_starmap_body", "A", "replace_with_vanilla"),
    TierRule("/Game/Libraries/MW5_TOI_Functions", "frontend_support_library", "A", "replace_with_vanilla"),
    TierRule("/Game/InnerSphereData/MW5_InnerSphereData", "innersphere_data", "B", "experiment_if_tier_a_fails"),
    TierRule(
        "/Game/InnerSphereData/Updated/EmployerInfoData",
        "employer_info_data",
        "B",
        "experiment_if_tier_a_fails",
    ),
    TierRule(
        "/Game/InnerSphereData/Updated/SystemFactionChanges",
        "system_faction_changes",
        "B",
        "experiment_if_tier_a_fails",
    ),
    TierRule(
        "/Game/UI/FrontEnd/Starmap/Materials/Factions/",
        "faction_materials",
        "C",
        "restore_only_if_needed",
    ),
    TierRule(
        "/Game/Campaign/CampaignArcs/BorderChanges/",
        "border_changes",
        "C",
        "restore_only_if_needed",
    ),
)


def classify_path(base_path: str) -> tuple[str, str, str]:
    if base_path.startswith("/Plugins/"):
        return "plugin_content", "-", "keep_tku"
    if base_path.startswith("/Game/Employers/"):
        return "employer_assets", "keep", "keep_tku"
    if base_path.startswith("/Game/Factions/"):
        return "faction_assets", "keep", "keep_tku"
    if base_path.startswith("/Game/Campaign/Personas/"):
        return "persona_assets", "keep", "keep_tku"
    for rule in TIER_RULES:
        if base_path.startswith(rule.prefix):
            return rule.domain, rule.patch_tier, rule.proposed_action
    if base_path.startswith("/Game/"):
        return "root_other", "review", "manual_review"
    return "unknown", "review", "manual_review"


def patch_description(max_tier: str, full_root_vanilla: bool = False) -> str:
    if full_root_vanilla:
        return (
            "Local MW5 v1.13.378 compatibility patch for TheKnownUniverse. "
            "This rescue build replaces every TKU root /Game asset that has a current vanilla counterpart, "
            "while leaving TKU-only plugin and custom content intact."
        )
    if max_tier == "A":
        return (
            "Local MW5 v1.13.378 compatibility patch for TheKnownUniverse. "
            "Tier A replaces stale frontend/starmap glue with current vanilla assets "
            "while leaving TKU plugin content and gameplay data intact."
        )
    if max_tier == "B":
        return (
            "Local MW5 v1.13.378 compatibility patch for TheKnownUniverse. "
            "Tier B extends the frontend rescue set with current vanilla InnerSphere data "
            "to reduce legacy starmap deserialization failures."
        )
    return (
        "Local MW5 v1.13.378 compatibility patch for TheKnownUniverse. "
        "This build includes the current vanilla rescue sets through Tier C."
    )


def tier_bases(base_paths: list[str], max_tier: str) -> list[str]:
    max_index = TIER_ORDER.index(max_tier)
    prefixes = [rule.prefix for rule in TIER_RULES if TIER_ORDER.index(rule.patch_tier) <= max_index]
    return [base for base in base_paths if any(base.startswith(prefix) for prefix in prefixes)]
