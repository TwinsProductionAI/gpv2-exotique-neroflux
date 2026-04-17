"""Deterministic routing logic for GPV2_EXOTIQUE_NEROFLUX."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

NUMERIC_FIELDS = (
    "emotion",
    "creativity",
    "logic",
    "symbolic_density",
    "context_density",
    "urgency",
)

ROUTE_KEYS = ("DreamCore", "Primordia", "RIME", "Emo+")


def clamp(value: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    """Clamp a float into the normalized signal range."""

    return max(minimum, min(maximum, value))


def normalize_packet(packet: dict[str, Any]) -> dict[str, Any]:
    """Return a normalized Neroflux packet.

    Numeric fields are coerced to floats and clamped between 0 and 1. Missing
    numeric fields become 0.0. This function returns a new dictionary and does not
    mutate the caller's input.
    """

    normalized = deepcopy(packet)

    intention = str(normalized.get("intention", "")).strip()
    if not intention:
        raise ValueError("Neroflux packet requires a non-empty 'intention'.")

    normalized["intention"] = intention

    for field in NUMERIC_FIELDS:
        raw_value = normalized.get(field, 0.0)
        try:
            normalized[field] = clamp(float(raw_value))
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Field '{field}' must be numeric.") from exc

    normalized["contradiction"] = bool(normalized.get("contradiction", False))
    return normalized


class NerofluxRouter:
    """Route cognitive packets between GPV2 Exotique submodules."""

    def route(self, packet: dict[str, Any]) -> dict[str, Any]:
        normalized = normalize_packet(packet)

        emotion = normalized["emotion"]
        creativity = normalized["creativity"]
        logic = normalized["logic"]
        symbolic_density = normalized["symbolic_density"]
        context_density = normalized["context_density"]
        urgency = normalized["urgency"]
        contradiction = normalized["contradiction"]

        load = {
            "emotional_load": round(emotion, 3),
            "creative_drift": round((creativity + symbolic_density) / 2, 3),
            "logical_pressure": round(max(logic, urgency, 1.0 if contradiction else 0.0), 3),
            "context_pressure": round(context_density, 3),
        }
        load["total"] = round(sum(load.values()) / 4, 3)

        routes = self._build_routes(
            emotion=emotion,
            creativity=creativity,
            logic=logic,
            symbolic_density=symbolic_density,
            context_density=context_density,
            urgency=urgency,
            contradiction=contradiction,
            total_load=load["total"],
        )
        channels = self._build_channels(routes, emotion)
        pace = self._select_pace(load, urgency, contradiction)
        actions = self._select_actions(load, routes, pace, contradiction)
        trace = self._build_trace(normalized, load, routes, pace, actions)

        dominant_route = max(routes, key=routes.get)

        return {
            "module": "GPV2_EXOTIQUE_NEROFLUX",
            "version": "0.1.0",
            "dominant_route": dominant_route,
            "pace": pace,
            "routes": routes,
            "channels": channels,
            "load": load,
            "actions": actions,
            "trace": trace,
        }

    def _build_routes(
        self,
        *,
        emotion: float,
        creativity: float,
        logic: float,
        symbolic_density: float,
        context_density: float,
        urgency: float,
        contradiction: bool,
        total_load: float,
    ) -> dict[str, float]:
        routes = {
            "DreamCore": 0.20 + (creativity * 0.38) + (symbolic_density * 0.24),
            "Primordia": 0.20 + (logic * 0.34) + (urgency * 0.30),
            "RIME": 0.20 + (context_density * 0.36) + (logic * 0.12),
            "Emo+": 0.20 + (emotion * 0.48),
        }

        if contradiction:
            routes["Primordia"] += 0.40
            routes["RIME"] += 0.10

        if total_load >= 0.72:
            routes["RIME"] += 0.16

        return self._normalize_weights(routes)

    def _build_channels(self, routes: dict[str, float], emotion: float) -> dict[str, float]:
        channels = {key: round(clamp(0.30 + weight), 3) for key, weight in routes.items()}

        if emotion >= 0.65:
            channels["Emo+"] = round(clamp(channels["Emo+"] + 0.18), 3)

        return channels

    def _select_pace(
        self,
        load: dict[str, float],
        urgency: float,
        contradiction: bool,
    ) -> str:
        if contradiction or urgency >= 0.75:
            return "fast"

        if load["emotional_load"] >= 0.65 and load["creative_drift"] >= 0.65:
            return "slow"

        if load["total"] >= 0.72:
            return "slow"

        return "balanced"

    def _select_actions(
        self,
        load: dict[str, float],
        routes: dict[str, float],
        pace: str,
        contradiction: bool,
    ) -> list[str]:
        actions: list[str] = []

        if load["emotional_load"] >= 0.65:
            actions.append("dilate_emo_channels")

        if load["creative_drift"] >= 0.65 and not contradiction:
            actions.append("permit_dreamcore_drift")

        if contradiction:
            actions.append("redirect_to_primordia_tribunal")

        if load["context_pressure"] >= 0.60 or load["total"] >= 0.72:
            actions.append("stabilize_with_rime")

        if pace == "slow":
            actions.append("reduce_exchange_velocity")

        if routes["Primordia"] >= 0.34:
            actions.append("preserve_logical_balance")

        if not actions:
            actions.append("maintain_balanced_circulation")

        return actions

    def _build_trace(
        self,
        packet: dict[str, Any],
        load: dict[str, float],
        routes: dict[str, float],
        pace: str,
        actions: list[str],
    ) -> list[str]:
        dominant_route = max(routes, key=routes.get)

        return [
            f"intention accepted: {packet['intention']}",
            f"total load evaluated at {load['total']}",
            f"dominant route selected: {dominant_route}",
            f"pace selected: {pace}",
            f"actions selected: {', '.join(actions)}",
        ]

    def _normalize_weights(self, routes: dict[str, float]) -> dict[str, float]:
        total = sum(routes.values())
        if total <= 0:
            return {key: round(1.0 / len(ROUTE_KEYS), 3) for key in ROUTE_KEYS}

        return {key: round(routes[key] / total, 3) for key in ROUTE_KEYS}
