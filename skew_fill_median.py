def skew_fill_median(data, column):
    from scipy.stats import skew
    if skew(data[column].dropna()) > 10:
        data[column] = data[column].apply(lambda x:data[column].mean() if x > data[column].mean() else x)
        print ('왜도 처리:', column)
#########################################333
for column in numeric:
    skew_fill_median(df,column)
