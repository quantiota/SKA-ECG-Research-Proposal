#!/usr/bin/env python3
"""MIT-BIH record 119, second order: Δt₂ and P₂ of every cycle-to-cycle step, coloured by the
MIT-BIH labels, read from the published label cube of SKA-ECG-Arrhythmia-Second-Order.

    python fig_mitdb119.py -> ../figures/mitdb119_labels.png
"""
import json, pathlib, re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent
CUBE = HERE.parents[1] / "SKA-ECG-Arrhythmia-Second-Order/mitdb/vr/ska2_ecg_mitdb119_scale25_scale25_label_vr.html"
COL = {"N→N": "#59a14f", "N→V": "#e15759", "V→N": "#4e79a7"}
NAME = {"N→N": "N→N  normal rhythm", "N→V": "N→V  coupling interval", "V→N": "V→N  compensatory pause"}

D = json.loads(re.search(r"const D\s*=\s*(\{.*?\});\n", CUBE.read_text(encoding="utf-8"), re.S).group(1))
d = pd.DataFrame({"k": D["k"], "dt": D["dt"], "p": D["p"], "lb": D["lb"]})
fig, ax = plt.subplots(1, 2, figsize=(14, 4.8))
for lb, c in COL.items():
    g = d[d.lb == lb]
    ax[0].scatter(g.k, g.dt / 1000, s=6, c=c, label=f"{NAME[lb]} ({len(g)})")
    ax[1].scatter(g.k, g.p, s=6, c=c)
ax[0].set_ylabel("Δt₂ = time between two cycles (s)"); ax[1].set_ylabel("P₂")
for a in ax:
    a.set_xlabel("cycle k"); a.grid(alpha=.3)
ax[0].legend(markerscale=3, loc="upper left", fontsize=9)
fig.suptitle("MIT-BIH record 119 (F, 51), second-order SKA learning, scale 25: steps coloured by the MIT-BIH labels")
fig.tight_layout()
out = HERE.parent / "figures" / "mitdb119_labels.png"
fig.savefig(out, dpi=110)
print(f"saved {out}")
