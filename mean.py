def h_mean(s):
    return len(s) / sum([1/x for x in s])
def g_mean(i):
    x = np.array(i)
    return x.prod()**(1.0/len(x))
  
# total.groupby('공구_상품명')['팔로워_유입율(%)'].agg(["mean", h_mean, g_mean]).reset_index()
