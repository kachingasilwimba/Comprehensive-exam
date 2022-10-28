#===================================================================
# Data Spliting 
#===================================================================
def timeslicing(Exp,Exp3,start_date, end_date, last_date):
    """
      Inputs
      ------
          start_date        str : the start date from which to extract
          end_date          str : the end date 
      outputs
      -------
    """
    
    #=====================Experiment 1,2,4a-d 
    X_training_exp = Exp.sel(time = slice(start_date, end_date))
    X_test_exp = Exp.sel(time = slice(end_date+1, last_date))  
    
    #===================== Experiment 3
    Y_trainging_exp3 = Exp3.sel(time=slice(start_date, end_date))
    Y_test_exp3 = Exp3.sel(time = slice(end_date+1, last_date))
    
    return X_training_exp, X_test_exp, Y_trainging_exp3, Y_test_exp3