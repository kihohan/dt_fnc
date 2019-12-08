Frequency Encoding
'''
Frequency encoding is a powerful technique that allows LGBM to see whether column values are rare or common. 
For example, if you want LGBM to "see" which credit cards are used infrequently, try
'''
def frequency_encoding(data,columns):
    temp = data[column].value_counts().to_dict()
    data[column] = data[column].map(temp)
