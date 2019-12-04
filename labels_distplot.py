def labels_distplot(data,labels,columns):
    df_1 = data[data[labels] == 0]
    df_2 = data[data[labels] == 1]
    sns.distplot(df_1[columns])
    sns.distplot(df_2[columns])
    plt.show()
#########################
distplot(dt,'labels','column')
