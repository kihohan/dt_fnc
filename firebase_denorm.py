'''
array([{'key': 'memberId', 'value': {'double_value': None, 'float_value': None, 'int_value': 71369.0, 'string_value': None}},
       {'key': 'firebase_screen_id', 'value': {'double_value': None, 'float_value': None, 'int_value': -5.844859139467282e+18, 'string_value': None}},
       {'key': 'firebase_conversion', 'value': {'double_value': None, 'float_value': None, 'int_value': 1.0, 'string_value': None}},
       {'key': 'ga_session_number', 'value': {'double_value': None, 'float_value': None, 'int_value': 13.0, 'string_value': None}},
       {'key': 'ga_session_id', 'value': {'double_value': None, 'float_value': None, 'int_value': 1658068138.0, 'string_value': None}},
       {'key': 'env', 'value': {'double_value': None, 'float_value': None, 'int_value': None, 'string_value': 'prod'}},
       {'key': 'categoryCode', 'value': {'double_value': None, 'float_value': None, 'int_value': None, 'string_value': 'MEETING'}},
       {'key': 'engaged_session_event', 'value': {'double_value': None, 'float_value': None, 'int_value': 1.0, 'string_value': None}},
       {'key': 'firebase_event_origin', 'value': {'double_value': None, 'float_value': None, 'int_value': None, 'string_value': 'app'}},
       {'key': 'firebase_screen_class', 'value': {'double_value': None, 'float_value': None, 'int_value': None, 'string_value': 'MainActivity'}}],
      dtype=object)

==>

{'memberId': '71369.0',
 'firebase_screen_id': '-5.844859139467282e+18',
 'firebase_conversion': '1.0',
 'ga_session_number': '13.0',
 'ga_session_id': '1658068138.0',
 'env': 'prod',
 'categoryCode': 'MEETING',
 'engaged_session_event': '1.0',
 'firebase_event_origin': 'app',
 'firebase_screen_class': 'MainActivity'}
'''
def extract_keys(array):
    res = [x['key'] for x in array]
    return res
    
def extract_value(_dict):
    return [x[1] for x in _dict.items() if x[1] != None]

def extract_values(_dict):
    array_values = [x['value'] for x in _dict]
    values = [extract_value(x) for x in array_values]
    res = np.array(values).flatten()
    return res

def decompose_array(nested_array):
    keys = extract_keys(nested_array)
    values = extract_values(nested_array)
    res = dict(zip(keys, values))
    return res
  
# res_df = pd.json_normalize(df_event['event_params'].apply(decompose_array))
