#!/bin/bash
#wann2J.py --elements Cr --efermi -0.87  --spinor --path ../../inputs/3_CrI3_wannier_SOC/data/x --prefix_spinor='wannier90' --kmesh 7 7 1  --nz 50 --groupby orbital --output_path result/TB2J_results_x
#wann2J.py --elements Cr --efermi -0.87  --spinor --path ../../inputs/3_CrI3_wannier_SOC/data/y --prefix_spinor='wannier90' --kmesh 7 7 1  --nz 50 --groupby orbital --output_path result/TB2J_results_y
#wann2J.py --elements Cr --efermi -0.87  --spinor --path ../../inputs/3_CrI3_wannier_SOC/data/z --prefix_spinor='wannier90' --kmesh 7 7 1  --nz 50 --groupby orbital --output_path result/TB2J_results_z
TB2J_merge.py -T structure  refs/TB2J_results_x refs/TB2J_results_y refs/TB2J_results_z --output_path result/TB2J_results
