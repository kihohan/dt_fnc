def percent_encoding(data,column_name,target,low_target,high_target):
    dt_column = data.groupby([column_name,target])[target].size().reset_index(name = 'cnt')
    items = []
    values = []
    for i in range(dt_column[column_name].nunique()):
        sm = dt_column[dt_column[column_name] == dt_column[column_name].unique()[i]]
        items.append(dt_column[column_name].unique()[i])
        try:
            percent = float(sm[sm[target] == high_target]['cnt'].values / sm[sm[target] == low_target]['cnt'].values)
            values.append(round(percent,2))
        except:
            values.append(0)
    dictionary = dict (zip(items,values))
    return df[column_name].map(dictionary).fillna(0)
#############################
df[column_name] = percent_encoding(df,'column_name','target',0,1)
