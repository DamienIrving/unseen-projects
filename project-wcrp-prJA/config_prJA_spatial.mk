# Configuration file for wcrp-prJA precip spatial analysis

PROJECT_NAME=wcrp-prJA
ENV_DIR=/g/data/xv83/dbi599/miniconda3/envs/unseen
PROJECT_DIR=/g/data/xv83/unseen-projects/outputs/wcrp-prJA

## Labels
METRIC=pr-jul-aug
REGION=asia
TIMESCALE=annual

## Metric calculation
VAR=pr
UNITS=mm day-1
TIME_FREQ=YE-DEC
METRIC_OPTIONS=--variables ${VAR} --lat_bnds -15 65 --lon_bnds 35 165 --months 7 8 --time_agg sum --time_freq ${TIME_FREQ} --input_freq D --time_agg_min_tsteps 40 --units ${VAR}='${UNITS}' --units_timing middle
METRIC_OPTIONS_FCST= --output_chunks lead_time=50




