# copernicus_downscale/hydro_timeseries.py
import cdsapi
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
import os

def download_era5_timeseries(year, variable, bbox, output_file):
    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'variable': variable,
            'year': str(year),
            'month': [f'{m:02}' for m in range(1, 13)],
            'day': ['01'],
            'time': ['00:00'],
            'format': 'netcdf',
            'area': bbox,
            'grid': [0.25, 0.25],
        },
        output_file
    )

def analyze_variable(netcdf_file, variable_name):
    ds = xr.open_dataset(netcdf_file)
    da = ds[variable_name].mean(dim=["longitude", "latitude"])
    df = da.to_dataframe().reset_index()
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)
    df.plot(title=f"{variable_name} over time", figsize=(10, 5))
    plt.ylabel(variable_name)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return df
