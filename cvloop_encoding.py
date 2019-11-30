def cvloop_encoding(data, column_name, target, method = 'mean'):
    from sklearn.model_selection import StratifiedKFold 
    from sklearn.model_selection import train_test_split

    train = df[~(df[target] == -1)]
    test = df[df[target] == -1]

    train, test = train_test_split(train, test_size = 0.2, random_state = 13, shuffle=True) 
    train_new = train.copy() 
    train_new[:] = np.nan 
    train_new[column_name] = np.nan

    X_train = train.drop(target, axis=1) 
    Y_train = train[target] 
    skf = StratifiedKFold(n_splits = 5, shuffle = True, random_state = 13)

    if method == 'mean':
        for tr_idx, val_idx in skf.split(X_train, Y_train): 
            X_train, X_val = train.iloc[tr_idx], train.iloc[val_idx] 
            means = X_val[column_name].map(X_train.groupby(column_name)[target].mean()) 
            X_val[column_name] = means 
            train_new.iloc[val_idx] = X_val
        global_mean = train[target].mean()
        result = train_new[column_name].fillna(global_mean)
    elif method == 'median':
        for tr_idx, val_idx in skf.split(X_train, Y_train): 
            X_train, X_val = train.iloc[tr_idx], train.iloc[val_idx] 
            medians = X_val[column_name].map(X_train.groupby(column_name)[target].median()) 
            X_val[column_name] = medians 
            train_new.iloc[val_idx] = X_val
        global_mean = train[target].median()
        result = train_new[column_name].fillna(global_mean)
    elif method == 'std':
        for tr_idx, val_idx in skf.split(X_train, Y_train): 
            X_train, X_val = train.iloc[tr_idx], train.iloc[val_idx] 
            stds = X_val[column_name].map(X_train.groupby(column_name)[target].std()) 
            X_val[column_name] = stds 
            train_new.iloc[val_idx] = X_val
        global_mean = train[target].std()
        result = train_new[column_name].fillna(global_mean)
    else:
        raise ValueError("Incorrect method supplied: '{}'. Must be one of 'mean', 'median', 'std'".format(method))
    return result
