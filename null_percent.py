def null_percent(data,data_2):
    for i in data.columns:
        print (i,':',round(data[i].isnull().sum() / len(data) * 100 ),'%', '||',
              i,':',round(data_2[i].isnull().sum() / len(data_2) * 100 ),'%')
################################33
null_percent(df_1,df_2)
