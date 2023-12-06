#importing importing libraries 

import netCDF4 as nc
import xarray as xr
import pandas as pd
import numpy as np
f1=('C:/Users/hp/Desktop/netcdf rainfall/merged_files1.nc')
ds=xr.open_dataset(f1)
ds
da=ds['RAINFALL']
da
ds = xr.open_dataset(f1)

variable_without_time = ds['RAINFALL'].isel(time=0)

#viewing the data 
variable_without_time

#merging 2020-2022 with time

file_paths = [
    'C:/Users/hp/Desktop/netcdf rainfall/2020.nc',
    'C:/Users/hp/Desktop/netcdf rainfall/2021.nc',
    'C:/Users/hp/Desktop/netcdf rainfall/2022.nc'
]

#merging 2020-2022 without time
datasets = [xr.open_dataset(file_path) for file_path in file_paths]
merged_dataset = xr.merge(datasets)
merged_dataset.to_netcdf('merged_file_without_common_dimension.nc')

#file locations 
file_paths = [
    'C:/Users/hp/Desktop/netcdf rainfall/merged_file_without_common_dimension.nc',
    'C:/Users/hp/Desktop/netcdf rainfall/RF_1901_2019-001.nc'
]


datasets = [xr.open_dataset(file_path) for file_path in file_paths]

merged_dataset = xr.merge(datasets)
merged_dataset.to_netcdf('merged_file_without_common_dimension.nc')

#renaming dimensions 
file1= 'C:/Users/hp/Desktop/netcdf rainfall/RF_1901_2019-001.nc'
ds=xr.open_dataset(file1)

ds= ds.rename({"lat": "LATITUDE", "lon": "LONGITUDE", "time": "TIME", "rf": "RAINFALL"})

ds
output_file_path=('C:/Users/hp/Desktop/netcdf rainfall/1901-2022f.nc')
ds.to_netcdf(output_file_path)



#final path
file_paths = [
    'C:/Users/hp/Desktop/netcdf rainfall/1901-2022f.nc',
    'C:/Users/hp/Desktop/netcdf rainfall/merged_file_without_common_dimension.nc'
]


datasets = [xr.open_dataset(file_path) for file_path in file_paths]

merged_dataset = xr.merge(datasets)
merged_dataset.to_netcdf('1901-2022.nc')
