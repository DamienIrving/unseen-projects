"""Create MIROC6 DCPP file lists"""

import glob
import os
import argparse

import numpy as np


file_dir = "/g/data/oi10/replicas/CMIP6/DCPP/MIROC/MIROC6/dcppA-hindcast"
freq_dict = {
    'pr': 'day',
    'sfcWind': 'day',
    'tos': 'Omon',
    'tasmax': 'day',
    'psl': 'day'
}


def create_file_list(var):
    """Create a file list"""

    outfile_name = f"MIROC6_dcppA-hindcast_{var}_files.txt"
    try:
        os.remove(outfile_name)
    except OSError:
        pass

    freq = freq_dict[var]
    nfiles = 10 if var == 'tos' else 20

    for year in np.arange(1960, 2018 + 1):
        infiles1 = glob.glob(f"{file_dir}/s{year}-r?i1p1f1/{freq}/{var}/gn/*/*.nc")
        infiles1.sort()
        infiles2 = glob.glob(f"{file_dir}/s{year}-r??i1p1f1/{freq}/{var}/gn/*/*.nc")
        infiles2.sort()
        infiles = infiles1 + infiles2
        assert len(infiles) == nfiles, f"year {year} does not have {nfiles} {var} files"
        with open(outfile_name, "a") as outfile:
            for item in infiles:
                outfile.write(f"{item}\n")


def main(args):
    """Run the program"""

    for var in args.vars:
        create_file_list(var)
   

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vars", type=str, nargs='*', help="Variables to process")
    args = parser.parse_args()
    main(args)

