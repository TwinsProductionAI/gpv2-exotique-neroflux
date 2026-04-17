# GPV2_EXOTIQUE_NEROFLUX

Version: `0.1.0`
Status: experimental

`GPV2_EXOTIQUE_NEROFLUX` is a cognitive-flow regulator for the GPV2 Exotique layer.
It does not generate content by itself. It modulates how internal signals circulate
between imagination, emotion, reflection, and judgment modules.

In the ORA vocabulary:

- `DreamCore` explores imagination, dream logic, and creative drift.
- `Primordia` arbitrates judgment, contradiction, and logical balance.
- `RIME` reflects, clarifies, and stabilizes dense reasoning.
- `Emo+` tracks emotional charge and affective intensity.
- `Neroflux` regulates speed, density, and routing between them.

## Purpose

Neroflux acts like a circulation protocol for thought packets. It receives a
structured cognitive state, evaluates load and pressure, then returns:

- target route weights for GPV2 submodules,
- recommended cognitive pace,
- channel dilation levels,
- stabilization actions,
- a compact trace of the routing decision.

## Minimal Example

```python
from gpv2_neroflux import NerofluxRouter

router = NerofluxRouter()

result = router.route({
    "intention": "Design a symbolic architecture for a creative AI module.",
    "emotion": 0.72,
    "creativity": 0.88,
    "logic": 0.55,
    "symbolic_density": 0.91,
    "context_density": 0.64,
    "urgency": 0.20,
})

print(result["dominant_route"])
print(result["pace"])
print(result["actions"])
```

## Local Development

This project has no runtime dependency.

```powershell
python -m unittest discover -s tests
```

## Repository Layout

```text
gpv2-exotique-neroflux/
|- README.md
|- MODULE.md
|- LICENSE
|- pyproject.toml
|- schemas/
|  `- neroflux.schema.json
|- src/
|  `- gpv2_neroflux/
|     |- __init__.py
|     `- neroflux.py
|- examples/
|  `- basic_flow.json
`- tests/
   `- test_neroflux.py
```

## Design Note

The module is intentionally deterministic in `v0.1.0`. This keeps traces stable,
testable, and easier to review before connecting it to a larger GPV2 runtime.
