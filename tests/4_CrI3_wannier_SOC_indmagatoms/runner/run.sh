#!/bin/bash
wann2J.py --efermi -0.87  --spinor --path ../../inputs/3_CrI3_wannier_SOC/data/z --prefix_spinor='wannier90' --kmesh 7 7 1  --nz 50 --groupby orbital --output_path result/TB2J_results_z --index_magnetic_atoms 1 --elements Cr
