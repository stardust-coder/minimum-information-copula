from datetime import datetime, date, timedelta
import pandas_datareader.data as web
import investpy
import math



def get_data_from_fred(start,end,code):
    ### fredから取得
    df = web.DataReader(code,"fred",start,end)
    return df

def get_data_from_stooq(start,end,ticker_symbol="7177"):
    ###stooqから取得
    #銘柄コード入力(7177はGMO-APです。)
    ticker_symbol_dr=ticker_symbol + ".JP"
    
    #データ取得
    df = web.DataReader(ticker_symbol_dr, data_source='stooq', start=start,end=end)
    #2列目に銘柄コード追加
    df.insert(0, "code", ticker_symbol, allow_duplicates=False)
    return df


def get_data_from_investpy(start,end):#investpy経由
    start_ = start.strftime('%d/%m/%Y')
    end_ = end.strftime('%d/%m/%Y')
    df = investpy.get_index_historical_data(index='DAX',country='germany',
                                        from_date=start_,to_date=end_)
    return df

def preprocessing(df):
    '''
    df: df with 2 columns
    return: df-os 2 columns, df with 4 columns
    '''
    cols = df.columns
    df_new = df.sort_values(by=cols[0])
    df_new[f"{cols[0]}-os"] = [(i+1)/(len(df)+1) for i in range(len(df))]
    df_new = df_new.sort_values(by=cols[1])
    df_new[f"{cols[1]}-os"] = [(i+1)/(len(df)+1) for i in range(len(df))]
    df_new = df_new.sort_index()
    return df_new.iloc[:,2:4], df_new

def log_return(df,target_col):
    ls = df.iloc[:,target_col]
    new_ls = [False]
    for i in range(len(ls)-1):
        r = math.log(ls[i+1]/ls[i])
        new_ls.append(r)
    df_new = df.copy()
    df_new["log-return"] = new_ls
    return df_new["log-return"][1:]

def normalize_ls(df): ###開始時刻を1とする.
    df_adj = df/df[0]
    return df_adj

def normalize_df(df): ###開始時刻を1とする.
    ls = df.iloc[:,0]
    ls_adj = ls/ls[0]
    df["adj"] = ls_adj
    return df["adj"]