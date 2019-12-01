def label_encoding(data,column_name):
    from sklearn.preprocessing import LabelEncoder
    items = list (data[column_name].values)
    le = LabelEncoder()
    le.fit(items)
    le_labels = le.transform(items)
    return le_labels
#################################33
df['column'] = label_encoding(df,'column')
