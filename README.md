# The Entropy Cube of the Heart

 [![arXiv](https://img.shields.io/badge/arXiv-2503.13942-b31b1b)](https://arxiv.org/abs/2503.13942)   [![arXiv](https://img.shields.io/badge/arXiv-2504.03214-b31b1b)](https://arxiv.org/abs/2504.03214)   [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-SKA-orange)](https://huggingface.co/quant-iota) [![Sponsor](https://img.shields.io/badge/Sponsor-quantiota-ea4aaa?logo=github-sponsors)](https://github.com/sponsors/quantiota)

**Structured Knowledge Accumulation on the Raw ECG Stream: Research Proposal**

The raw ECG is read as an ordered stream of waves, P → Q → R → S → T, and each wave is one step of
the SKA real-time learner. The proposal sets the entropy cube (z, ż, H) as the standard object of
a heart, summarises what is registered so far on public PhysioNet databases, and proposes a
monitoring set-up that learns one loop per hour or per day.

**[Read the proposal (PDF)](SKA-ECG-Research-Proposal.pdf)**

## Files

| file | content |
|---|---|
| [`SKA-ECG-Research-Proposal.pdf`](SKA-ECG-Research-Proposal.pdf) | the proposal |
| [`proposal.md`](proposal.md) | its source (`pandoc proposal.md -o SKA-ECG-Research-Proposal.pdf --pdf-engine=pdflatex`) |
| [`figures/`](figures/) | the figures, from the SKA ECG repositories |
| [`scripts/fig_mitdb119.py`](scripts/fig_mitdb119.py) | Figure 3, from the published label cube of record 119 |

The results, figures and cubes are in the SKA ECG repositories listed in Section 9 of the proposal.
The SKA real-time engine is proprietary and is not included.

## License

MIT
