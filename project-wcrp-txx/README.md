## WCRP TXx

The [common event attribution and assessment (CEAA) project](https://www.wcrp-climate.org/epesc-wg3/epesc-wg3-ceaa)
of the WCRP Explaining and Predicting Earth System Change (EPESC) Lighthouse Activity
seeks to identify extreme weather and climate events for coordinated study.

This repository contains the analysis related to our submission
to the 2021 Pacific Northwest Heatwave case study.
The [guidance note](https://docs.google.com/document/d/1Ww_oW_ynmPco3cbG18hO9fdoFwH6VA7HPRyXGiCUryU/edit?usp=sharing)
explains the submission requirements.

### Data processing

```
make metric-obs PROJECT_DETAILS=project-wcrp-txx/txx_config.mk OBS_DETAILS=dataset_makefiles/ERA5-tasmax_config.mk
```

```
make metric-forecast MODEL=CanESM5 PROJECT_DETAILS=project-wcrp-txx/txx_config.mk MODEL_DETAILS=dataset_makefiles/CanESM5_dcppA-hindcast_config.mk OBS_DETAILS=dataset_makefiles/ERA5-tasmax_config.mk
```
