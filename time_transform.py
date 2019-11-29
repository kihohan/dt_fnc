def time_transform(data, column_name):
    data[column_name]  = pd.to_datetime(data[column_name])
    data['year'] = data[colum_name].dt.year 
    data['month'] = data[colum_name].dt.month
    data['date'] = data[colum_name].dt.day
    data['day']  = data[colum_name].dt.weekday
    data['hour'] = data[colum_name].dt.hour
    data['minute'] = data[colum_name].dt.minute
    data['second'] = data[colum_name].dt.second
  
