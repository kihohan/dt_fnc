def smoothing_target_encoder(df, column, target, weight=100):
    
    train = df[~(df[target] == -1)]
    test = df[df[target] == -1]
    
    mean = df[target].mean()

    agg = df.groupby(column)[target].agg(['count', 'mean'])
    counts = agg['count']
    means = agg['mean']

    smooth = round((counts * means + weight * mean) / (counts + weight),2)
    
    train = train[column].map(smooth)
    test = test[column].map(smooth)
    result = pd.concat([train, test])
    
    return result
#################################################3
for column in encoding_list:
    df[column] = smoothing_target_encoder(df, column, 'label')
