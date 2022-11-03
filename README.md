 Integrating EOFs into Machine Learning Algorithms to Emulate Climate Land Model
 --------------------------
 This repository provides the code and Synthenthis paper (`Comprehensive_Synthesis_Paper.pdf`) for the comprehensive exam computing artifact in Computing Ph.D. (data science) at Boise State University. The code emulates and analyzes Climate Land Model version 5 (CLM5) simulations (`soil moisture`) using machine learning, neural networks, and empirical orthogonal functional analysis (EOFs). 

 

 Requirements
 -------------
 Install [EOFs package](https://github.com/ajdawson/eofs) for the empirical orthogonal finctional analysis.
 
 install [tensorflow](https://www.tensorflow.org/) and [keras](https://keras.io/) packages for neural networks and machine learning.
 
 install [xarray](http://xarray.pydata.org) to read the netCDF dataset and for preprocessing.
 
 Dataset
 -------
 The dataset used in this analysis is the CLM5 simulation generated under the Soil Parameter Intercomparison Project (SP-MIP) to assess soil parameters' influence on the variability of the Land Surface Model. The dataset was subsetted from the global CLM5 simulation available for download at `ftp://sp-mip2017@data.iac.ethc.ch`. The approach used to simulate the SPMIP dataset can be found in the [SPMIP documentation](https://www.gewexevents.org/wp-content/uploads/GLASS2017_SP-MIP_Protocol.pdfhttps://www.gewexevents.org/wp-content/uploads/GLASS2017_SP-MIP_Protocol.pdf). 
 
 Data Processing Files
 ----------------------
 The `EOFsfunction.py` calculates the empirical orthogal functions analysis and recostructs the dataset.
 
 The `Soil_moisture_weights.py` calculates the weighted average of soil moisture.
 
 The `packages.py`loads the modules needed for the data analysis.
 
 The `data_spliting.py` splits the data into train and test.
 
EOFs Analysis
--------------
The `Empirical_orthogal_function_analysis.ipynb` calculates the EOFs and visualize.

Machine Learning File
---------------------
The `Machine_learning_models.ipynb` emulates the CLM5 output (soil moisture) and integrates the EOFs into machine learning.

Seed Papers
------------
1. Dagon, K., B. M. Sanderson, R. A. Fisher, and D. M. Lawrence (2020). A machine learning
approach to emulation and biophysical parameter estimation with the community land model,
version 5. Advances in Statistical Climatology, Meteorology and Oceanography 6 (2), 223–244.


Citation
---------
- [eofs reseach paper](http://doi.org/10.5334/jors.122)

- [eofs libraly](http://dx.doi.org/10.5281/zenodo.46871)

