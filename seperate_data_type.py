def seperate_data_type(data,standard):
    binominal = []
    continuous = []
    for i in data.columns:
        if data[i].nunique() < standard:
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
###############################3
binominal_list,continuous_list = seperate_data_type(df,300)
