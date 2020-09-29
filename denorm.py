'''
[[
    {'raw_id': 214865513,   'reg_id': 'SERVER',   'reg_dt': datetime.datetime(2020, 8, 1, 1, 8, 33),   'stock_amount': -999,   'add_price': 7700,   'deal_type': ''},
    {'raw_id': 215089017,   'reg_id': 'SERVER',   'reg_dt': datetime.datetime(2020, 8, 1, 13, 13),   'stock_amount': -999,   'add_price': 7700,   'deal_type': ''}
]]

==>
[['T_ssg_585142_2674372588125794073',  Timestamp('2020-08-01 00:46:10'),  -999,  8910],
 ['T_ssg_585142_2674372588125794073',  Timestamp('2020-08-01 12:50:12'),  -999,  8910],
 ['T_ssg_585142_2674372588125794073',  Timestamp('2020-08-02 00:51:46'),  -999,  8910],
 ['T_ssg_585142_2674372588125794073',  Timestamp('2020-08-02 12:43:37'),  -999,  8910],
...
]
'''

def denorm_row(r, denorm_column):
    '''
        denorm_column : denormalize 할 column (1개의 컬럼만 denormalize 한다고 가정함)
        common_columns : denorm_column을 제외한 나머지 컬럼들
    '''
    common_columns = list(r.index)
    common_columns.remove(denorm_column)
    
    dict_list = []
    for item in r[denorm_column]: # denorm_column 의 모든 dict element에 대해서 
        item.update({key : r[key] for key in common_columns}) # common_columns를 중복으로 채워줌
        dict_list.append(item)
        
    return dict_list # dataframe의 하나의 row가 denormalize 된 list of dict

def denorm_df(norm_df, denorm_column):
    dl_series = norm_df.apply(lambda r : denorm_row(r, denorm_column), axis=1)
    denorm_df = pd.DataFrame([d for dl in dl_series for d in dl])
    return denorm_df
