# -*- coding: utf-8 -*-
"""
This module contains classes and functions for plotting data.
"""

from __future__ import division, print_function
import matplotlib.pyplot as plt
from .processing import *
import os


def plot_torque(ax=None, fig=None, save=False, savetype=".pdf",
                savedir="Figures", **kwargs):
    """Plot mean turbine torque versus mean turbine RPM."""
    s = Section("Perf")
    df = s.data
    if ax is None:
        fig, ax = plt.subplots()
    ax.plot(df.rpm, df.torque, **kwargs)
    ax.set_xlabel("RPM")
    ax.set_ylabel("Torque (Nm)")
    if fig is not None:
        fig.tight_layout()
    if save:
        if not os.path.isdir(savedir):
            os.makedirs(savedir)
        fig.savefig(os.path.join(savedir, "torque" + savetype))


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
