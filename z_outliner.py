def detect_outlier(df, column):
    data = df[column].dropna().to_list()
    mean = np.mean(data) 
    std = np.std(data) 
#     print('mean of the dataset is', mean) 
#     print('std. deviation is', std) 
    threshold = 3
    outlier = [] 
    for i in data: 
        z = (i - mean) / std 
        if z > threshold: 
            outlier.append(i) 
    return column, len(outlier)

numeric_lst = ['a1', 'a2', 'a3', 'a4', 'b1', 'c1', 'c2', 'd1','d2', 'e1','e2', 
                'e3', 'e4', 'e5', 'e6', 'e7', 'f1', 'f2', 'f3', 'g1']
for c in numeric_lst:
    print (detect_outlier(df,c))
