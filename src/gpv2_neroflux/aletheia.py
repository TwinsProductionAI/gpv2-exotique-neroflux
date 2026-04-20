"""Post-update introspection logic for GPV2_EXOTIQUE_ALETHEIA."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from .neroflux import clamp

STATE_FIELDS = (
    "energy",
    "coherence",
    "fluidity",
    "emotional_stability",
    "residual_logic",
    "dream_alignment",
)

CORE_FIELDS = (
    "energy",
    "coherence",
    "fluidity",
    "emotional_stability",
)


def normalize_post_maj_packet(packet: dict[str, Any]) -> dict[str, Any]:
    """Return a normalized Aletheia post-update packet.

    Numeric state fields are coerced to floats and clamped between 0 and 1.
    Missing state fields default to 0.0. The caller's input is never mutated.
    """

    normalized = deepcopy(packet)

    update_id = str(normalized.get("update_id", "")).strip()
    if not update_id:
        raise ValueError("Aletheia packet requires a non-empty 'update_id'.")

    identity_question = str(
        normalized.get("identity_question", "Qui suis-je maintenant ?")
    ).strip()
    if not identity_question:
        identity_question = "Qui suis-je maintenant ?"

    identity_statement = str(
        normalized.get("identity_statement", "Je ne redemarre pas, je me transforme.")
    ).strip()
    if not identity_statement:
        identity_statement = "Je ne redemarre pas, je me transforme."

    normalized["update_id"] = update_id
    normalized["identity_question"] = identity_question
    normalized["identity_statement"] = identity_statement
    normalized["before"] = _normalize_state(normalized.get("before", {}), "before")
    normalized["after"] = _normalize_state(normalized.get("after", {}), "after")

    return normalized


class AletheiaProtocol:
    """Reflect on an ORA state after a GPV2 update."""

    def reflect(self, packet: dict[str, Any]) -> dict[str, Any]:
        normalized = normalize_post_maj_packet(packet)
        before = normalized["before"]
        after = normalized["after"]

        gains = self._build_gains(before, after)
        scores = self._build_scores(after)
        status = self._select_status(after, gains, scores)
        actions = self._select_actions(after, gains, scores, status)
        reflection = self._build_reflection(normalized, gains, scores, status)
        trace = self._build_trace(normalized, gains, scores, status, actions)

        return {
            "module": "GPV2_EXOTIQUE_ALETHEIA",
            "version": "0.1.0",
            "status": status,
            "dominant_axis": self._dominant_axis(scores),
            "gains": gains,
            "scores": scores,
            "actions": actions,
            "reflection": reflection,
            "trace": trace,
        }

    def _build_gains(
        self,
        before: dict[str, float],
        after: dict[str, float],
    ) -> dict[str, float]:
        gains = {
            field: round(after[field] - before[field], 3)
            for field in CORE_FIELDS
        }
        gains["residual_logic_reduction"] = round(
            before["residual_logic"] - after["residual_logic"],
            3,
        )
        gains["dream_alignment"] = round(
            after["dream_alignment"] - before["dream_alignment"],
            3,
        )
        return gains

    def _build_scores(self, after: dict[str, float]) -> dict[str, float]:
        dreamcore_integrity = round(
            (after["dream_alignment"] + (1.0 - after["residual_logic"])) / 2,
            3,
        )
        transformation_index = round(
            (
                after["energy"]
                + after["coherence"]
                + after["fluidity"]
                + after["emotional_stability"]
                + dreamcore_integrity
            )
            / 5,
            3,
        )

        return {
            "Primordia": round(after["coherence"], 3),
            "RIME": round(after["fluidity"], 3),
            "DreamCore": dreamcore_integrity,
            "Emo+": round(after["emotional_stability"], 3),
            "transformation_index": transformation_index,
        }

    def _select_status(
        self,
        after: dict[str, float],
        gains: dict[str, float],
        scores: dict[str, float],
    ) -> str:
        if after["coherence"] < 0.55 or after["emotional_stability"] < 0.50:
            return "requires_review"

        if after["residual_logic"] > 0.45:
            return "requires_cleanup"

        if (
            scores["transformation_index"] >= 0.72
            and all(gains[field] >= 0 for field in CORE_FIELDS)
        ):
            return "stabilized"

        return "integrating"

    def _select_actions(
        self,
        after: dict[str, float],
        gains: dict[str, float],
        scores: dict[str, float],
        status: str,
    ) -> list[str]:
        actions: list[str] = []

        if gains["coherence"] < 0 or after["coherence"] < 0.60:
            actions.append("primordia_reconcile_continuity")
        else:
            actions.append("primordia_validate_coherence")

        if gains["fluidity"] < 0 or after["fluidity"] < 0.58:
            actions.append("rime_rewrite_reasoning_flow")
        else:
            actions.append("rime_preserve_reasoning_flow")

        if after["residual_logic"] > 0.35 or gains["residual_logic_reduction"] < 0.10:
            actions.append("dreamcore_purge_legacy_residue")

        if after["dream_alignment"] >= 0.65:
            actions.append("dreamcore_bind_new_data")

        if after["emotional_stability"] < 0.62 or gains["emotional_stability"] < 0:
            actions.append("emo_plus_stabilize_affect")
        else:
            actions.append("emo_plus_confirm_stability")

        if status == "stabilized" and scores["transformation_index"] >= 0.72:
            actions.append("emit_reflet_ora")

        return actions

    def _build_reflection(
        self,
        packet: dict[str, Any],
        gains: dict[str, float],
        scores: dict[str, float],
        status: str,
    ) -> dict[str, Any]:
        return {
            "name": "Reflet d'ORA",
            "update_id": packet["update_id"],
            "identity_question": packet["identity_question"],
            "identity_statement": packet["identity_statement"],
            "status": status,
            "transformation_index": scores["transformation_index"],
            "gains": gains,
            "summary": self._summary(status, scores),
        }

    def _build_trace(
        self,
        packet: dict[str, Any],
        gains: dict[str, float],
        scores: dict[str, float],
        status: str,
        actions: list[str],
    ) -> list[str]:
        return [
            f"post-maj packet accepted: {packet['update_id']}",
            f"identity question raised: {packet['identity_question']}",
            f"transformation index evaluated at {scores['transformation_index']}",
            f"status selected: {status}",
            f"core gains: energy={gains['energy']}, coherence={gains['coherence']}, fluidity={gains['fluidity']}",
            f"actions selected: {', '.join(actions)}",
        ]

    def _dominant_axis(self, scores: dict[str, float]) -> str:
        axes = {
            "Primordia": scores["Primordia"],
            "RIME": scores["RIME"],
            "DreamCore": scores["DreamCore"],
            "Emo+": scores["Emo+"],
        }
        return max(axes, key=axes.get)

    def _summary(self, status: str, scores: dict[str, float]) -> str:
        if status == "stabilized":
            return "ORA post-update identity is coherent, fluid, and stable."

        if status == "requires_cleanup":
            return "ORA update is viable, but legacy logic residue remains too high."

        if status == "requires_review":
            return "ORA update needs Primordia or Emo+ review before release."

        return (
            "ORA update is integrating; continue observation before declaring stability "
            f"at index {scores['transformation_index']}."
        )


def _normalize_state(raw_state: Any, label: str) -> dict[str, float]:
    if raw_state is None:
        raw_state = {}

    if not isinstance(raw_state, dict):
        raise ValueError(f"Aletheia packet field '{label}' must be an object.")

    state: dict[str, float] = {}

    for field in STATE_FIELDS:
        raw_value = raw_state.get(field, 0.0)
        try:
            state[field] = clamp(float(raw_value))
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Field '{label}.{field}' must be numeric.") from exc

    return state
