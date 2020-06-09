import pandas as pd
import os
import jieba
from utils import file_name_listdir
from functools import reduce

train_corpus = "../toy_data/train_docs.txt"
curr_path ="./"

dftrain = pd.read_csv(train_corpus,sep="\n")
# dfsql = pd.read_csv()

# print('original corpus data info:')
# print(dftrain.head())
# print(dftrain.shape)
# print("")


sql_raw_path = '../toy_data/sql_data/'
sql_path_list = file_name_listdir(sql_raw_path)
print("num of sql files:",len(sql_path_list))


sql_file = os.path.join(sql_raw_path,"result.txt")
sqls = []
with open(sql_file, "w+") as outfile:
    for f in sql_path_list:
        with open(os.path.join(sql_raw_path,f), "r") as infile:
            line = [x.strip() for x in infile.readlines()]
            resplit_line = reduce(list.__add__,[x.split(' ') for x in line])
        outfile.write('\n'.join(resplit_line))
    # print('last line',resplit_line)

df_sql = pd.read_csv(sql_file,'\n')
print('merged sql data info:')
print(df_sql.head())
print(df_sql.shape)
print("")


