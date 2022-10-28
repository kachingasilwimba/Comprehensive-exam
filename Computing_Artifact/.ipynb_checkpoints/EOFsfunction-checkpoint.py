import collections
collections.Iterable = collections.abc.Iterable


import eofs as eof
from eofs.xarray import Eof
from eofs.examples import example_data_path
from scipy import signal
import os
import numpy as np
from scipy import signal
import numpy.polynomial.polynomial as poly
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from eofs.standard import Eof

#===========================================================================
# Empirical Orthogal function Analysis 
#===========================================================================

import collections
collections.Iterable = collections.abc.Iterable

def Emp_Ortho_Funcs(SPMIP_data, n_eof):
    '''
    The function computes the empirical orthogonal functions and the corresponding time series by 
    initializing an EOF solver to do the EOF analysis. The Square-root of cosine of latitude weights
    are applied before the computation of EOFs from the data. In this presentation the EOFs has no
    unit and is dimensionaless. The project field projects the SPMIP data onto the EOFs to generate 
    a corresponding set of pseudo-PCs.
    '''
     
    "....Extracting SPMIP Data Shape ...."
    #=======================Extracting the shape of the SPMIP data 
    if len(SPMIP_data.shape) == 4:
        nt,nlat,nlon,ndepth = SPMIP_data.shape
    elif len(SPMIP_data.shape) == 3:
        nt,nlat,nlon = SPMIP_data.shape
    #=======================Detranding the SPMIP data 
    SPMIP_detrend = signal.detrend(SPMIP_data,axis=0, type='constant',bp=0)
    
    print("...Detrending the Data by removing the time-mean...")
    SPMIP_season = np.mean(SPMIP_detrend,axis=0)
    SPMIP_diff = SPMIP_detrend - SPMIP_season
        
    if len(SPMIP_data.shape) == 4:
        SPMIP_detrend = SPMIP_detrend.reshape((nt,ndepth,nlat,nlon), order='F')
    elif len(SPMIP_data.shape) == 3:
        SPMIP_detrend = SPMIP_detrend.reshape((nt,nlat,nlon), order='F') 
       
    print("....Checking Setting Weighting...")
    '''
    Create an EOF solver to do the EOF analysis. Square-root of cosine of 
    latitude weights are applied before the computation of EOFs.
    '''
    #=======================Square-root of cosine of latitude weights
    lats = SPMIP_data['lat'].data
    lons = SPMIP_data['lon'].data
    coslat = np.cos(np.deg2rad(lats[:]))
    wgts = np.sqrt(coslat)[..., np.newaxis]
    wgts=np.repeat(wgts[None,...],lons.shape[0],0).squeeze().T
    wgts = np.expand_dims(wgts,axis=0)
    
    ".....Initializing EOFs Solver...."
    if len(SPMIP_detrend.shape) == 4:           
        solver = Eof(SPMIP_detrend[:,:,:,:], weights=wgts,center=False) #initializing the EOFs object
    elif len(SPMIP_detrend.shape) == 3:
        solver = Eof(SPMIP_detrend[:,:,:], weights=wgts) #initializing the EOFs object
            
    print("....Decomposing Modes of SPMIP Data...")   
     #=======================Extracting EOFs modes from the SPMIP data and reconstructing the data 
    eofs = solver.eofs(neofs=n_eof,eofscaling=1)           # Empirical orthogonal functions (EOFs)
    pcs  = solver.pcs(npcs=n_eof, pcscaling=1).round(5)
    var_fracs = solver.varianceFraction()                  # Fractional EOF mode variances
    lambdas = solver.eigenvalues()                         # Eigenvalues (decreasing variances) associated with each EOF.
    errors = solver.northTest()                            # Typical errors for eigenvalues
    eofs_corr = solver.eofsAsCorrelation(neofs=n_eof)      # Correlation map EOFs 
    eofs_cov = solver.eofsAsCovariance(neofs=n_eof)        # Covariance map EOFs
    total_variance = solver.totalAnomalyVariance()
    pseudo_pcs = solver.projectField(SPMIP_detrend, neofs=n_eof) # Project a field onto the EOFs
    pseudo_pcs = (pseudo_pcs/np.std(pseudo_pcs,axis=0))
    reconstruction = solver.reconstructedField(n_eof)      # Reconstructed data field based on a subset of EOFs
    weights = solver.getWeights()                          # Weights used for the analysis
    
    print('...Correlating.....')
    #=======================Correlating EOFs time series with the SPMIP detraded data  
    '''
    Correlating the principal component of an EOF with the original time series at each
    data point.
    '''
    eof_corrpcs = np.zeros([n_eof,SPMIP_detrend.shape[1],SPMIP_detrend.shape[2]])
    for lat in range(SPMIP_detrend.shape[1]):
        for lon in range(SPMIP_detrend.shape[2]):
            for i in range(n_eof):
                eof_corrpcs[i,lat,lon]=np.corrcoef(pseudo_pcs[:,0],SPMIP_detrend[:,lat,lon])[0,1]
    
    return eofs, pcs, var_fracs, lambdas, eofs_corr, eof_corrpcs, reconstruction