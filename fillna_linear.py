def fillna_linear(data,time_column,column_name):
    data[time_column] = pd.to_datetime(data[time_column])
    data = data.sort_values(by = time_column)
    data[column_name] = data[column_name].interpolate(method = 'linear')
################################33
for column_name in weather:
    fillna_linear(df,'time_column',column_name)
