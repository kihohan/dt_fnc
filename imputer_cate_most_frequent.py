def imputer_cate_most_frequent(data,column_name):
    data[column_name] = data[column_name].fillna(data[column_name].value_counts().index[0])
#############################33
for column_name in cate_list:
    imputer_cate_most_frequent(df,column_name)
