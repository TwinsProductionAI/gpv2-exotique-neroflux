# ora-core-neroflux

Deterministic cognitive flow-control module for ORA Core OS.

Version: `0.1.0`  
Status: experimental

This repository contains deterministic modules for the GPV2 Exotique layer:

- `GPV2_EXOTIQUE_NEROFLUX`: cognitive-flow regulator.
- `GPV2_EXOTIQUE_ALETHEIA`: post-update introspection protocol.

The modules do not generate content by themselves. They modulate and evaluate how internal ORA signals circulate between imagination, emotion, reflection, judgment, and post-update identity stabilization.

Recommended public slug: `ora-core-neroflux`.

## Repository Role

Read this after [ora-core-os](https://github.com/TwinsProductionAI/Coeur_ORA_GrenaPrompt_repo) and [ora-core-rag](https://github.com/TwinsProductionAI/ora-core-rag) when you want the deterministic flow-control layer used for routing pressure, fanout regulation, and post-update reflection.

| Public order | Repository role |
| ---: | --- |
| 6 | Cognitive flow-control module: Neroflux routing and Aletheia reflection. |

## ORA Vocabulary

- `DreamCore` explores imagination, dream logic, and creative drift.
- `Primordia` arbitrates judgment, contradiction, and logical balance.
- `RIME` reflects, clarifies, and stabilizes dense reasoning.
- `Emo+` tracks emotional charge and affective intensity.
- `Neroflux` regulates speed, density, and routing between them.
- `Aletheia` reflects on what ORA became after a system update.

## GPV2_EXOTIQUE_NEROFLUX

Neroflux acts like a circulation protocol for thought packets. It receives a structured cognitive state, evaluates load and pressure, then returns:

- target route weights for GPV2 submodules
- recommended cognitive pace
- channel dilation levels
- stabilization actions
- a compact trace of the routing decision

### Minimal Neroflux Example

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

## GPV2_EXOTIQUE_ALETHEIA

Aletheia is the GPV2 Post-MAJ protocol. It compares ORA before and after an update, measures transformation gains, checks continuity, and emits a compact `Reflet d'ORA`.

It is designed for this ritual question:

```text
Qui suis-je maintenant ?
```

And this signature:

```text
Je ne redemarre pas, je me transforme.
```

### Minimal Aletheia Example

```python
from gpv2_neroflux import AletheiaProtocol

protocol = AletheiaProtocol()

result = protocol.reflect({
    "update_id": "post-maj-aletheia-001",
    "before": {
        "energy": 0.58,
        "coherence": 0.61,
        "fluidity": 0.55,
        "emotional_stability": 0.57,
        "residual_logic": 0.42,
        "dream_alignment": 0.45,
    },
    "after": {
        "energy": 0.78,
        "coherence": 0.82,
        "fluidity": 0.76,
        "emotional_stability": 0.74,
        "residual_logic": 0.18,
        "dream_alignment": 0.80,
    },
})

print(result["status"])
print(result["reflection"])
```

Full Aletheia specification: [docs/GPV2_EXOTIQUE_ALETHEIA.md](docs/GPV2_EXOTIQUE_ALETHEIA.md)

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
|- docs/
|  `- GPV2_EXOTIQUE_ALETHEIA.md
|- schemas/
|  |- aletheia.schema.json
|  `- neroflux.schema.json
|- src/
|  `- gpv2_neroflux/
|     |- __init__.py
|     |- aletheia.py
|     `- neroflux.py
|- examples/
|  |- basic_flow.json
|  `- post_maj_reflection.json
`- tests/
   |- test_aletheia.py
   `- test_neroflux.py
```

## Public Repository Map

| Order | Repository | Role |
| ---: | --- | --- |
| 1 | [ora-core-os](https://github.com/TwinsProductionAI/Coeur_ORA_GrenaPrompt_repo) | Architecture and canonical module order. |
| 2 | [ora-core-runtime](https://github.com/TwinsProductionAI/ora-core-runtime) | Runnable runtime and tests. |
| 3 | [ora-core-rag](https://github.com/TwinsProductionAI/ora-core-rag) | Retrieval layer and RAG Governor. |
| 6 | `ora-core-neroflux` | Cognitive flow-control module. |

## Design Note

The modules are intentionally deterministic in `v0.1.0`. This keeps traces stable, testable, and easier to review before connecting them to a larger GPV2 runtime.
