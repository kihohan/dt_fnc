def feature_type(data):
    binominal = []
    continuous = []
    for i in data.columns:
        if data[i].dtype == 'object':
            binominal.append(i)
        else:
            continuous.append(i)
    print ('binominal_data:', len(binominal), '개')
    print ('binominal_data:', binominal)
    print ('-------------------------------------------------------------------------------')
    #binominal_data = data[binominal]
    print ('continuous_data:', len(continuous), '개')
    print ('continuous_data:', continuous)
    #continuous_data = data[continuous]
    return binominal,continuous
##########################
binominal_list,continuous_list = feature_type(df)
 
