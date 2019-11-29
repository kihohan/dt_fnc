def dummy_data(data, columns):
    for column in columns:
        data = pd.concat([data, pd.get_dummies(data[column], prefix = column)], axis=1)
        data = data.drop(column, axis=1)
    return data
#############################3
dummy_columns = list (set(binominal_list) - set([label_class]))
df = dummy_data(df, dummy_columns)
