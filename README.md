 Integrating EOFs into Machine Learning Algorithms to Emulate Climate Land Model
 --------------------------
 This respository provides the code for the comprehensive exam computing artifact in Computing Ph.D. (data science) at Boise State University. The code emulates and analyze Climate Land Model version 5 (CLM5) output using machine learaning, neural networks and empirical orthogal fucntional analysis (Soil Moisture)
.
 

 Requirements
 -------------
 Install [EOF package](https://github.com/ajdawson/eofs) for the empirical orthogonal finctional analysis.
 
 install [tensorflow](https://www.tensorflow.org/) and [keras](https://keras.io/) packages for neural networks and machine learning.
 
 Dataset
 -------
 The dataset used in this analysis is the CLM5 simulation which was generated under the Soil Paramater Intercomparison Project (SP-MIP) with the aim of assessing the influence of soil parameters on the viriability of Land Surface Model. The dataset used was subseted from the global CLM5 simulation available for download at [SM-PMIP data](ftp://sp-mip2017@data.iac.ethc.ch). The approch used to simulate the dataset can be found in the [SPMIP documentation](https://www.gewexevents.org/wp-content/uploads/GLASS2017_SP-MIP_Protocol.pdfhttps://www.gewexevents.org/wp-content/uploads/GLASS2017_SP-MIP_Protocol.pdf)  
