def mm_scale(data,column_name):
    from sklearn.preprocessing import MinMaxScaler
    scale = MinMaxScaler().fit_transform(np.array(data[column_name]).reshape(-1, 1)).flatten()
    data[column_name] = scale

def ma_scale(data,column_name):
    from sklearn.preprocessing import MaxAbsScaler
    scale = MaxAbsScaler().fit_transform(np.array(data[column_name]).reshape(-1, 1)).flatten()
    data[column_name] = scale

def r_scale(data,column_name):
    from sklearn.preprocessing import RobustScaler
    scale = RobustScaler().fit_transform(np.array(data[column_name]).reshape(-1, 1)).flatten()
    data[column_name] = scale

def s_scale(data,column_name):
    from sklearn.preprocessing import StandardScaler
    scale = StandardScaler().fit_transform(np.array(data[column_name]).reshape(-1, 1)).flatten()
    data[column_name] = scale
#########################
for column_name in scale_list:
    mm_scale(data,column_name)
############################################
for column_name in continuous_list:
    mm_scale(dt,column_name)
