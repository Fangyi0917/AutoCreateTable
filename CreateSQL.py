#@ Author = wfy
#@ Date = 2019.10.11


import os
import sys
import pandas as pd
import argparse


def createSQL(name, comment, csvfile):
    print("CREATE TABLE %s (" % (name))
    df = pd.read_csv( csvfile, encoding = 'gb2312')
    df['数据格式'] = ""
    #print(df.shape)
    for col in range(len(df)):
        if df.loc[col]["类型"] == "TN":
            df.loc[col]["数据格式"] = "tinyint"
        elif df.loc[col]["类型"] == "TT":
            df.loc[col]["数据格式"] = "varchar(100)"
        elif df.loc[col]["类型"] == "N":
            df.loc[col]["数据格式"] = "int"
        elif df.loc[col]["类型"] == "自定义":
            df.loc[col]["数据格式"] = "varchar(500)"
        elif df.loc[col]["类型"] == "ID":
            df.loc[col]["数据格式"] = "varchar(20)"
        elif df.loc[col]["类型"] == "D":
            df.loc[col]["数据格式"] = "date"
        elif df.loc[col]["类型"] == "DT":
            df.loc[col]["数据格式"] = "datetime"
        elif df.loc[col]["类型"] == "F":
            df.loc[col]["数据格式"] = "float"
        elif df.loc[col]["类型"] == "BB":
            df.loc[col]["数据格式"] = "blob"
        elif str(df.loc[col]["类型"])[0] == "C":
            if df.loc[col]["类型"][1] == "B":
                df.loc[col]["数据格式"] = "varchar(500)"
            else:
                df.loc[col]["数据格式"] = "varchar(" + df.iloc[col]["类型"][1:] + ")"
        # if df.loc[col]["是否允许空"] == "是":
        #     df.loc[col]["是否允许空"] = "NULL"
        # if df.loc[col]["是否允许空"] == "否":
        #     df.loc[col]["是否允许空"] = "NOT NULL"
        if col == 0:
            sql = df.iloc[col]["标识"].lower() + "  " +  df.iloc[col]["数据格式"] \
                + "  " + "PRIMARY KEY  NOT NULL  COMMENT" + "  " +"\'"+ df.loc[col]["数据元名称"] +"\'" + ','
        elif col == len(df)-1:
            sql =  df.iloc[col]["标识"].lower() + "  " +  df.iloc[col]["数据格式"] \
                +"  " + "COMMENT" + "  " + "\'"+ df.loc[col]["数据元名称"] +"\'"
        else:
            sql =  str(df.iloc[col]["标识"]).lower() + "  " +  df.iloc[col]["数据格式"] \
                +"  " + "COMMENT" + "  " + "\'"+ df.loc[col]["数据元名称"] +"\'" + ','
        print(sql)
    print(") COMMENT = '%s'" % (comment))
    print('\n\n\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--tbname", help = "请输入表名",  type = str)
    parser.add_argument("--comment", help = "请输入表名注释", type = str)
    parser.add_argument("--csvfile", help = "包含数据源名称、标识、类型的文件名",  type = str)
    args = parser.parse_args()
    createSQL(args.tbname, args.comment, args.csvfile)
    
