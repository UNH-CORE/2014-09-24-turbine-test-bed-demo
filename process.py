#!/usr/bin/env python
"""
This script runs processing functions from `Modules.processing`.
"""

from __future__ import print_function
import Modules.processing as pr


if __name__ == "__main__":
    print("Processing all data")
    pr.batch_process_all(nproc=1)
