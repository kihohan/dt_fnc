def imputer_cont_trim_mean(data,column_name):
    from scipy import stats
    try:
        data[column_name] = data[column_name].fillna(stats.trim_mean(data[column_name].dropna(), 0.2))
        data[column_name] = round(data[column_name],2)
    except:
        print ('not_changed ->',column_name)
 ########################
for column_name in data:
    imputer_cont_trim_mean(data,column_name)
