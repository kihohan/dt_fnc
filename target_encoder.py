def target_encoder(df, column, target, index=None, method='std'):
    # 테스트셋 섞이지 않게
    train = df[~(df[target] == -1)]
    test = df[df[target] == -1]
    # 결측치 확인
    index = train.index if index is None else index 
    # 인코딩 종류
    if method == 'mean':
        encoded_column = train[column].map(train.iloc[index].groupby(column)[target].mean())
        dict_ = dict (train.iloc[index].groupby(column)[target].mean())
        test[column] = test[column].map(dict_)
    elif method == 'median':
        encoded_column = train[column].map(train.iloc[index].groupby(column)[target].median())
        dict_ = dict (train.iloc[index].groupby(column)[target].median())
        test[column] = test[column].map(dict_)
    elif method == 'std':
        encoded_column = train[column].map(train.iloc[index].groupby(column)[target].std())
        dict_ = dict (train.iloc[index].groupby(column)[target].std())
        test[column] = test[column].map(dict_)
    else:
        raise ValueError("Incorrect method supplied: '{}'. Must be one of 'mean', 'median', 'std'".format(method))
    
    result = pd.concat([encoded_column, test[column]])
    return result
#########################################################
for column in encoding_list:
    df[column] = target_encoder(df, column, 'label', index=None, method='std')
