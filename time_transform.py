def time_transform(data, column_name):
    data[column_name]  = pd.to_datetime(data[column_name])
    data['year'] = data[column_name].dt.year 
    data['month'] = data[column_name].dt.month
    data['dates'] = data[column_name].dt.day
    data['days']  = data[column_name].dt.weekday
    data['hour'] = data[column_name].dt.hour
    data['minute'] = data[column_name].dt.minute
    data['second'] = data[column_name].dt.second
    data = data.drop(column_name,1)
    return data
##########################
df = time_transform(df, 'date')
df = df.drop('date',1)
