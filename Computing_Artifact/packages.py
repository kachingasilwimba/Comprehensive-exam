import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from netCDF4 import Dataset
import netCDF4
import time
import pandas as pd
import matplotlib.pyplot as plt, numpy as np
from matplotlib.colors import BoundaryNorm
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import xarray as xr
import sys, glob, os
import warnings
import matplotlib.colors as colors              
from matplotlib.patches import Patch
warnings.filterwarnings("ignore")
import cartopy.feature as cfeature
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable


from sklearn.svm import SVR
from sklearn.linear_model import BayesianRidge,LinearRegression,ElasticNet
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import explained_variance_score,mean_absolute_error,mean_squared_error,r2_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler,Normalizer
from sklearn.metrics import r2_score, mean_squared_error,mean_absolute_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import collections
import datetime as dt
import time


#======================
from sklearn.neighbors import NearestNeighbors
from sklearn import neighbors
from sklearn.metrics import mean_squared_error 
from math import sqrt
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
#===============================
import collections
import time
import os
import datetime as dt
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import warnings
from numpy import newaxis
from keras.layers import LSTM, Dense, Dropout, GRU
from keras.models import Sequential
from tensorflow.keras.optimizers import SGD, Adagrad, RMSprop,Adam
from sklearn.preprocessing import MinMaxScaler, StandardScaler,Normalizer
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from keras.regularizers import l2
#==================================
import eofs as eof
from eofs.xarray import Eof
from eofs.examples import example_data_path
from scipy import signal
import os
import numpy as np
from scipy import signal
import numpy.polynomial.polynomial as poly
from mpl_toolkits.basemap import Basemap
from eofs.standard import Eof