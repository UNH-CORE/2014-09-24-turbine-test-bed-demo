"""
Download all raw data from the experiment. Should be executed with IPython
from the experiment root directory, i.e.,

    ipython Scripts/download.py

Currently, all data will be overwritten even if it already exists.
"""

from __future__ import division, print_function
import json
import Modules.processing as pr
import os
import sys
import progressbar

if sys.version_info[0] == 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve


if __name__ == "__main__":
    # Download all files in test plan
    tp = pr.load_test_plan()

    for s_name, s_tp in tp.items():
        for i, run in s_tp.iterrows():
            pr.download_raw(s_name, run.run, "nidata")
            pr.download_raw(s_name, run.run, "acsdata")
            if run.vectrino:
                pr.download_raw(s_name, run.run, "vecdata")
            if "fbg" in run:
                if run.fbg:
                    pr.download_raw(s_name, run.run, "fbgdata")

    # Download shakedown data
    with open("Config/raw_data_urls.json") as f:
        urls = json.load(f)

    for fname, url in urls.items():
        if fname.split("_")[0] == "Shakedown":
            nrun = fname.split("_")[1]
            local_fname = fname.split("_")[-1]
            print("Downloading {} from Shakedown run {}".format(local_fname,
                                                                nrun))
            local_dir = os.path.join("Data", "Raw", "Shakedown", nrun)
            # Create local dir if it doesn't exist
            if not os.path.isdir(local_dir):
                os.makedirs(local_dir)
            local_fpath = os.path.join(local_dir, local_fname)
            pbar = progressbar.ProgressBar()
            def download_progress(blocks_transferred, block_size, total_size):
                percent = int(blocks_transferred*block_size*100/total_size)
                try:
                    pbar.update(percent)
                except ValueError:
                    pass
                except AssertionError:
                    pass
            pbar.start()
            urlretrieve(url, local_fpath, reporthook=download_progress)
            pbar.finish()
