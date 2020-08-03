import tqdm
from multiprocessing import Pool, Manager
from multiprocessing.dummy import Pool as ThreadPool, Manager as ThreadManager

class mp():
    '''
    multi-processing interface
    '''
    def __init__(self, task_func, param_list, n_process=4, using_tqdm=False, tqdm_desc='mp2'):
        self.task_func = task_func
        self.param_list = param_list
        self.n_process = n_process
        self.using_tqdm = using_tqdm
        self.tqdm_desc = tqdm_desc
        
    def run(self):
        self.result = []
        with Pool(self.n_process) as pool, Manager() as manager:
            # communication channel between process / with parent
            # predefined codes
            # 1. 'break' : True - stop all children and return 
            comm = manager.dict()
            self.param_list = [(comm, p) for p in self.param_list]
            
            if self.using_tqdm: # first come first out. ie. unordered result
                for r in tqdm.tqdm(pool.imap_unordered(self.task_func, self.param_list), total=len(self.param_list), desc=self.tqdm_desc):
                    self.result.append(r)
            else: # ordered result
                for r in pool.map(self.task_func, self.param_list):
                    self.result.append(r)
                    
        return self.result
        
df_size = 50000
df_chunk = [df[i*df_size:(i+1)*df_size] for i in range(len(df) // df_size + 1)]
len(df_chunk)
# function
def mp_clean_spm(p):
    # dataframe type
    _, x = p
    x.loc[:, 'mall_goods_name'] = [' '.join(clean_spm(sp.encode_as_pieces(x))) for x in x['mall_goods_name']]
    return x
    
r = mp(mp_clean_spm, df_chunk, 8, True).run()
result = pd.concat(r).sort_index()
