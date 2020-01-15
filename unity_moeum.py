def unity_moeum(x):
    # !pip install hgtk
    import hgtk
    decompose = hgtk.text.decompose(x)
    replace = decompose.replace('ㅐ','ㅔ') # 사전 구축 필요해
    result = hgtk.text.compose(replace)
    return result
