def label_encoding(data,column_name):
    from sklearn.preprocessing import LabelEncoder
    items = list (data[column_name].values)
    le = LabelEncoder()
    le.fit(items)
    le_labels = le.transform(items)
    data[column_name] = le_labels
