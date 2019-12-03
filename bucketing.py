# after scaling -> bucketing numeric data
def bucketing(series, n = 7):
    from itertools import chain
    lst = series.astype('f').sort_values()
    division = len(lst) / n
    result = [lst[round(division * i):round(division * (i + 1))] for i in range(n)]
    new = []
    for i in range(len(result)):
        new.append([i+1 for x in result[i]])
    new = list(chain(*new))
    return new
#########################################
for column in numeric_list:
    df_2 = df_2.sort_values(by = column, ascending = False)
    df_2[column] = bucketing(df_2[column])
