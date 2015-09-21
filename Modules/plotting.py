# -*- coding: utf-8 -*-
"""
This module contains classes and functions for plotting data.
"""

from __future__ import division, print_function
from Modules.processing import *
import os


def plot_vertical_lines(xlist, ymaxscale=1, color="gray"):
    if not isinstance(xlist, list):
        x = [x]
    ymin = plt.axis()[2]
    ymax = plt.axis()[3]*ymaxscale
    for x in xlist:
        plt.vlines(x, ymin, ymax,
                   color=color, linestyles="dashed")
    plt.ylim((ymin, ymax))


def watermark(ax=None):
    """Create a "preliminary" watermark on plots."""
    if ax is None:
        ax = plt.gca()
    plt.text(0.5, 0.5,"PRELIMINARY\nDO NOT PUBLISH",
             horizontalalignment="center",
             verticalalignment="center",
             transform=ax.transAxes,
             alpha=0.2,
             fontsize=32,
             zorder=10)
