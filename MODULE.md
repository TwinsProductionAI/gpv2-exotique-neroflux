# GPV2_EXOTIQUE_NEROFLUX Module Specification

Version: `0.1.0`
Status: experimental specification

## Definition

`GPV2_EXOTIQUE_NEROFLUX` is the flow-regulation protocol of the GPV2 Exotique
layer. Its role is to regulate speed, density, and direction of internal exchanges
between `DreamCore`, `Primordia`, `RIME`, and `Emo+`.

It does not produce memory, final truth, or raw text generation. It produces
circulation decisions.

## Conceptual Model

Neroflux represents the vital flow of the ORA overlay:

- when emotional charge rises, `Emo+` channels dilate;
- when creative drift is useful, `DreamCore` receives more flow and the pace slows;
- when contradiction or urgency appears, `Primordia` receives priority;
- when density or ambiguity rises, `RIME` stabilizes and clarifies the signal.

## Inputs

All numeric inputs are normalized between `0.0` and `1.0`.

| Field | Type | Required | Meaning |
| --- | --- | --- | --- |
| `intention` | string | yes | User or system intent to route. |
| `emotion` | number | no | Emotional load. |
| `creativity` | number | no | Need for creative drift. |
| `logic` | number | no | Need for strict reasoning. |
| `symbolic_density` | number | no | Symbolic or metaphorical density. |
| `context_density` | number | no | Amount of contextual pressure. |
| `urgency` | number | no | Need for fast arbitration. |
| `contradiction` | boolean | no | Whether a contradiction has been detected. |

Missing numeric fields default to `0.0`. `contradiction` defaults to `false`.

## Outputs

| Field | Type | Meaning |
| --- | --- | --- |
| `dominant_route` | string | Highest-weight target module. |
| `pace` | string | `slow`, `balanced`, or `fast`. |
| `routes` | object | Weight per target module. |
| `channels` | object | Channel dilation per target module. |
| `load` | object | Derived load metrics. |
| `actions` | array | Stabilization or routing actions. |
| `trace` | array | Human-readable routing trace. |

## Routing Rules

1. High emotion increases `Emo+` channel dilation.
2. High creativity or symbolic density increases `DreamCore`.
3. High logic, urgency, or contradiction increases `Primordia`.
4. High context density increases `RIME`.
5. When creative and emotional loads are both high, pace slows to avoid overload.
6. When urgency or contradiction is high, pace becomes fast and `Primordia` is prioritized.
7. When total load is too high, `RIME` receives additional stabilization weight.

## Modes

The current implementation exposes deterministic routing only. Future versions may
formalize named modes:

- `EXOTIQUE_SOFT`: creative but close to real-world structure.
- `EXOTIQUE_SYMBOLIQUE`: metaphorical and symbolic architecture.
- `EXOTIQUE_ONIRIQUE`: DreamCore-dominant associative exploration.
- `EXOTIQUE_TRIBUNAL`: Primordia-dominant judgment and arbitration.

## Non-Goals

- It is not a language model.
- It is not a memory store.
- It is not an emotional classifier.
- It is not a truth engine.

Neroflux is a regulator. It determines how the thought flow should circulate before
a downstream module produces a final answer.
