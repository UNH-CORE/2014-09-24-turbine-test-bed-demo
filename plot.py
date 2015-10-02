#!/usr/bin/env python
"""
This script generates the relevant figures and/or tables from the experiment. To
reprocess the data, run `process.py`.
"""

import py_2015_09_24_turbine_test_bed_demo.plotting as pl
from pxl.styleplot import set_sns
import matplotlib.pyplot as plt

save = True
savetype = ".pdf"
show = True


if __name__ == "__main__":
    # Set plot style using PXL's Seaborn wrapper
    set_sns(rc={"axes.grid": True, "lines.linewidth": 2})

    # Call plotting functions here
    pl.plot_torque(marker="o", save=save, savetype=savetype)
    fig, ax = plt.subplots()
    pl.plot_torque(ax)

    if show:
        plt.show()
