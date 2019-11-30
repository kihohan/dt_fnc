def percnet_graph(data,column_name,label):
    dt = data[[column_name,label]].dropna().groupby([column_name,label]).size().reset_index(name = 'cnt')
    feature_list = []
    percent_list = []
    for i in range(dt[column_name].nunique()):
        item = dt[dt[column_name] == dt[column_name].unique()[i]]
        feature = dt[column_name].unique()[i]
        try:
            percent = round (item[item[label] == 'Y']['cnt'].values[0] / item['cnt'].sum() * 100)
            feature_list.append(feature)
            percent_list.append(percent)
        except:
            pass
    result = pd.DataFrame({column_name:feature_list,
                           'percent':percent_list}).sort_values(by = 'percent', ascending = False)
    result = result[result['percent'] > 50]
    plt.figure(figsize = (15,5))
    plt.subplot(1,2,1)
    sns.countplot(data = data ,x = column_name,hue = label)
    plt.xticks(rotation = 90)
    plt.legend(bbox_to_anchor=(1.0, 1.05))
    plt.subplot(1,2,2)
    sns.barplot(data = result, x = column_name, y = 'percent', palette="Blues_d")
    plt.xticks(rotation = 90)
    plt.show()
################################
percnet_graph(train,'column_name','label')
