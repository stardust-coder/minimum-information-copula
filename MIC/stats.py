#Calculate statistics of the given data
from scipy import stats
from scipy.stats import rv_continuous, rv_histogram, norm, beta, multivariate_normal
from scipy.stats import norm

def lower_tail(df,u,verbose=True):
    numall = len(df)
    df_sorted_x = df.sort_values(by=df.columns[0])
    df_sorted_x = df_sorted_x.iloc[:int(numall*u),:]
    thre_x = df_sorted_x.iloc[-1,0]
    df_sorted_y = df.sort_values(by=df.columns[1])
    df_sorted_y = df_sorted_y.iloc[:int(numall*u),:]
    thre_y = df_sorted_y.iloc[-1,1]
    if verbose:
        print(f"u={u},Threshold: {thre_x},{thre_y}")
    df_both = df.copy()
    df_both.columns = ["x","y"]
    df_both = df_both.query("x <= @thre_x & y <= @thre_y")
    if verbose:
        print("λL:", len(df_both)/int(numall*u))
    return len(df_both)/int(numall*u)

def upper_tail(df,u,verbose=True):
    numall = len(df)
    df_sorted_x = df.sort_values(by=df.columns[0],ascending=False)
    df_sorted_x = df_sorted_x.iloc[:int(numall*u),:]
    thre_x = df_sorted_x.iloc[-1,0]
    df_sorted_y = df.sort_values(by=df.columns[1],ascending=False)
    df_sorted_y = df_sorted_y.iloc[:int(numall*u),:]
    thre_y = df_sorted_y.iloc[-1,1]
    if verbose:
        print(f"u={u},Threshold: {thre_x},{thre_y}")
    df_both = df.copy()
    df_both.columns = ["x","y"]
    df_both = df_both.query("x >= @thre_x & y >= @thre_y")
    if verbose:
        print("λU:", len(df_both)/int(numall*u))
    return len(df_both)/int(numall*u)


def calc_bivar_stats(df):
    '''
    Input:
    df: 2 columns
    
    Return:
    rho, tau, ll5, ll1, lu5, lu1
    '''
    t = stats.kendalltau(df.iloc[:,0].tolist(), df.iloc[:,1].tolist())
    r = stats.spearmanr(df.iloc[:,0].tolist(), df.iloc[:,1].tolist())
    return t,r,lower_tail(df,0.05),lower_tail(df,0.01),upper_tail(df,0.05),upper_tail(df,0.01)
