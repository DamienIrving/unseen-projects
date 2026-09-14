"""Script for producing a tier1 data file"""
import pdb
import argparse
from datetime import datetime, timezone
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import xarray as xr
import cmdline_provenance as cmdprov


rp_dict = {}
rp_dict['txx'] = {
    'BCC-CSM2-MR': 4840,
    'CanESM5': 1261,
#    'CMCC-CM2-SR5': ,
#    'EC-Earth3': ,
#    'IPSL-CM6A-LR': ,
#    'MIROC6': ,
#    'MPI-ESM1-2-HR': ,
#    'MRI-ESM2-0': ,
#    'NorCPM1': 
}
rp_dict['rx1day'] = {
#    'BCC-CSM2-MR': ,
#    'CanESM5': ,
#    'CMCC-CM2-SR5': ,
#    'EC-Earth3': ,
#    'IPSL-CM6A-LR': ,
#    'MIROC6': ,
#    'MPI-ESM1-2-HR': ,
#    'MRI-ESM2-0': ,
#    'NorCPM1': 
}

percentiles = [5, 16, 84, 95]
rp_bnds_dict = {}
rp_bnds_dict['txx'] = {
    'BCC-CSM2-MR': (2223, 2943, 10200, 20348),
    'CanESM5': (904, 1026, 1586, 1870),
#    'CMCC-CM2-SR5': (),
#    'EC-Earth3': (),
#    'IPSL-CM6A-LR': (),
#    'MIROC6': (),
#    'MPI-ESM1-2-HR': (),
#    'MRI-ESM2-0': (),
#    'NorCPM1': (),
}
rp_bnds_dict['rx1dy'] = {
#    'BCC-CSM2-MR': (),
#    'CanESM5': (),
#    'CMCC-CM2-SR5': (),
#    'EC-Earth3': (),
#    'IPSL-CM6A-LR': (),
#    'MIROC6': (),
#    'MPI-ESM1-2-HR': (),
#    'MRI-ESM2-0': (),
#    'NorCPM1': (),
}

code_url = 'https://github.com/AusClimateService/unseen-projects/tree/master/project-wcrp-txx'
history_log = cmdprov.new_log(code_url=code_url)
global_attrs = {
    'institution': 'CSIRO',
    'method': 'UNSEEN',
    'event': 'PNW Heatwave',
    'data_tier': 'tier1',
    'project': 'WCRP Common Event Attribution and Assessment',
    'contact': 'damien.irving@csiro.au',
    'experiment': 'dcppA-hindcast',
    'references': 'Decadal Climate Prediction Project (https://doi.org/10.5194/gmd-9-3751-2016)',
#    'processing': '',
    'creation_date': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'history': history_log,
}

event_definitions = {
    'txx': '39.51 degC'
#    'rx1day': ''
}


def get_encoding(ds):
    """Output file encoding."""

    encoding = {}
    ds_vars = list(ds.coords) + list(ds.keys())
    for ds_var in ds_vars:
        encoding[ds_var] = {'_FillValue': None}

    return encoding


def main(args):
    """Run the program"""

    models = list(rp_dict[args.metric].keys())
    rp_values = list(rp_dict[args.metric].values())
    rp_bnds_values = np.array(list(rp_dict[args.metric].values()))

    rp_da = xr.DataArray(
        data=rp_values,
        coords={'model': models,},
        name='rp',
        attrs = {
            'standard_name': 'return_period',
            'long_name': f'return period of a {event_definitions[args.metric]} event in the year 2021',
            'units': 'years',
        }
    )
    pdb.set_trace()
    rp_bnds_da = xr.DataArray(
        data=rp_bnds_values,
        coords={'model': models, 'percentile': percentiles},
        name='rp_bnds',
        attrs = {
            'long_name': 'return period uncertainty bounds',
            'units': 'years'
        }
    )
    output_ds = xr.merge([rp_da, rp_bnds_da])
    output_ds.attrs = global_attrs
    output_ds['model'].attrs['long_name'] = 'Model name'
    output_ds['percentile'].attrs['long_name'] = 'Percentile'

    outdir = f'/g/data/xv83/unseen-projects/outputs/wcrp-{args.metric}/data'
    fname = f'{outdir}/CSIRO_UNSEEN_tier1.nc'
    encoding = get_encoding(output_ds)
    output_ds.to_netcdf(fname, encoding=encoding)
    print(fname)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        argument_default=argparse.SUPPRESS,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )                      
    parser.add_argument("metric", type=str, choices=('txx', 'rx1day'), help="metric")           
    args = parser.parse_args()
    main(args)
