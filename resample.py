def resample(Train_X,Train_Y):
    import imblearn.under_sampling as usam
    import imblearn.over_sampling as osam 
    # ros = osam.RandomOverSampler()
    # SMOTEos = osam.SMOTE(k_neighbors = 5)
    # B_SMOTEos = osam.SMOTE(k_neighbors = 5, m_neighbors = 5)
    # A_SMOTEos = osam.ADASYN(n_neighbors = 5)
    # rus = usam.RandomUnderSampler()
    erus = usam.CondensedNearestNeighbour(n_neighbors = 3, n_jobs = 1)
    # nrus1 = usam.NearMiss(n_neighbors = 3, version = 1)
    sampled_X, sampled_Y = erus.fit_sample(Train_X, Train_Y)
    Train_X = pd.DataFrame(sampled_X, columns = Train_X.columns)
    Train_Y = pd.DataFrame(sampled_Y, columns = Train_Y.columns)
    return Train_X, Train_Y
################################
Train_X, Train_Y = resample(Train_X,Train_Y)
