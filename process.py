#!/usr/bin/env python
"""
This script runs processing functions.
"""

from __future__ import print_function
import py_2015_09_24_turbine_test_bed_demo.processing as pr


if __name__ == "__main__":
    print("Processing all data")
    pr.batch_process_all(nproc=1)
