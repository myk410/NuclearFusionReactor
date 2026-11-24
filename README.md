# Nuclear Fusion Reactor

A continuing scientific investigation of sustained **whole-facility net electrical fusion energy**, including conventional and unconventional mechanisms and plant-wide enabling technologies.

Start with [ResearchIndex](ResearchIndex.md), [ProjectStatus](ProjectStatus.md) and [Continuation](Progress/Continuation.md). [Permanent standards](AGENTS.md) and [stage acceptance gates](Research/Charter.md) govern future work.

## Current research
- [Preliminary plant rankings](Rankings/Master.md): high-field D–T tokamaks and optimized stellarators are close leading baselines.
- [Executed calculations](Simulations/Findings.md) and [additional inference/tradeoff results](Simulations/InferenceAndTradeoffs.json).
- [Initial literature synthesis](LiteratureReviews/Overview.md), [source ledger](References/Bibliography.md), [hypotheses](Research/Hypotheses.md) and [skeptical audit](ScientificCriticism/RedTeam.md).
- [Interim synthesis](FinalReports/InterimSynthesis.md). Comprehensive final reports remain pending.

33 dossiers include 19 candidate plant architectures, 12 enabling interventions and two scientific testbeds. This is not 33 complete reactor designs. Scores are subjective comparisons, not probabilities. No new physical discovery or validated power plant is claimed.

## Reproduce
From a Python 3 environment, with no external dependencies:

```sh
python3 ComputationalModels/analyze.py
python3 ComputationalModels/inference_and_tradeoffs.py
python3 ComputationalModels/verify_repository.py
```

The models write deterministic results under Simulations and Rankings. They study accounting, synthetic uncertainty, statistical identifiability and scoring, not plasma evolution or reactor operation. Input assumptions, units and limitations are explicit. No binaries, paper archives or redundant backups are required.
