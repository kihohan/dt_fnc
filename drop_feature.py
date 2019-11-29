def drop_feature(data, column_name, drop_rate = 0.6):
    percent = data[column_name].isnull().sum() / len(data) 
    print ('{0}: {1}'.format(column_name,round(percent,2)))
    if percent >= drop_rate:
        del df[column_name]
        print ('---------->DELETE: {0}'.format(column_name))
