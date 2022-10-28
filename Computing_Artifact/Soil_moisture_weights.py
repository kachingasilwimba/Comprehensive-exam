import numpy as np
from netCDF4 import Dataset
import netCDF4
import xarray as xr
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt


def soil_weighted_ave(CLM5_data):
    
    """
    Computing the weight for the water content for the soil layers. The takes 
    Climate land model output for the soil moisture and computes the weight for the root zone.
    
    returns
    The soilmoiture weighted average
    """
    
    delta_z  = np.array([0.020,0.040,0.060,0.080,0.120,0.160,0.200,0.240,0.280]) #layer thickness
    levsoil = [0,1,2,3,4,5,6,7,8,9,10]     # selected 6 layers 
    theta = np.zeros(len(levsoil))          # average water content per unit layer
    
    for n_layer in range(len(levsoil)):
        "theta is the volumatric water content at each soil layer"
        theta[n_layer] = CLM5_data.mrlsl.sel(levsoi=slice(n_layer,n_layer+1)).mean().values
                                                                   
    unit_depth_water = np.sum(theta)/1000    # 1000kg/m^3 is the density of water gives Unit depth of water
    sum_delta_z = np.sum(delta_z)            # summing the layer node depth
    soilm_weighted_ave = unit_depth_water/sum_delta_z    #  soil moisture layer weighted sum
    return soilm_weighted_ave