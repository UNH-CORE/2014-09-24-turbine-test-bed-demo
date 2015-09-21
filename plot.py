#!/usr/bin/env python
"""
This script generates the relevant figures and/or tables from the experiment. To
reprocess the data, run `process.py`.
"""

import os
from Modules.plotting import *
from pxl.styleplot import set_sns

save = True
savetype = ".pdf"
show = True


if __name__ == "__main__":
    # Set plot style using PXL's Seaborn wrapper
    set_sns()

    # Call plotting functions here

    if show:
        plt.show()
