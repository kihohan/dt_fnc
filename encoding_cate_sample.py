df['column'] = df['column'].fillna('NAN')
def encoding_cate(x):
    if x in ['A', 'B', 'C', 'D', 'E', 'F', 'D']:
        return x
    else:
        return 'etc'
df['column'] = df['column'].apply(encoding_cate)
