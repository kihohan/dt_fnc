def word_graph(word_series,word_count):
    from itertools import chain
    import seaborn as sns

    word_list = [x for x in word_series]
    list_ = list (chain(*[x.split(' ') for x in word_list]))
    u_list = list (set(list_))
    c_list = [list_.count(x) for x in u_list]
    data = pd.DataFrame({'word':u_list,'count':c_list}).sort_values(by = 'count', ascending = False).head(word_count)
    plt.figure(figsize = (20,5))
    plt.subplot(1,2,1)
    sns.barplot(data = data, x = 'word', y = 'count', color = 'g')
    plt.title('word_count')
    plt.subplot(1,2,2)
    sns.distplot(c_list, color = 'r')
    plt.title('count_distplot')
    plt.xticks(rotation = 90)
    plt.show()
