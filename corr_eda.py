def corr_eda(data,threshold):
    corr_matrix = data.corr()
    for column in corr_matrix.columns:
        dict_ = corr_matrix[column].to_dict() 
        print ({key: value for key, value in dict_.items() if (value > threshold) | (value < -threshold)})
        print ('----------------------')
#######################################################
corr_eda(df, 0.5)
