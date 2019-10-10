
import os
import sys
import pandas as pd

# #SQL格式
# CREATE TABLE azbj_bffaxxb(
#   id INT PRIMARY KEY not null COMMENT '学号',
#   name VARCHAR(200) COMMENT '姓名',
#   age    int COMMENT '年龄'
# ) COMMENT='学生信息'


#从word中抽取表名、属性名、类型、长度、是否为空、是否主键、注释
azbj_table_name = ["azbj_bffaxxb", "azbj_bffazxxxb", "azbj_wcnznxxcjb", "azbj_jtcyxxb", "azbj_bjxzxxcjb","azbj_gzjlcjb","azbj_bjxxcjb","azbj_azxxcjb",
                    ]
azbj_table_comment = ["帮扶方案信息表", "帮扶方案执行信息表", "未成年子女信息采集表", "家庭成员信息表", "帮教小组信息采集表", "工作记录采集表", "帮教信息采集表", "安置信息采集表",]
#azbj_table_file = ["azbj_bffaxxb.csv", "azbj_bffazxxxb.csv", "azbj_wcnznxxcjb.csv", "azbj_jtcyxxb.csv", "azbj_bjxzxxcjb.csv","azbj_gzjlcjb.csv","azbj_bjxxcjb.csv","azbj_azxxcjb.csv"]
for i in range(len(azbj_table_name)):
    print("CREATE TABLE %s (" % (azbj_table_name[i]))

    df = pd.read_csv( "Table/" + azbj_table_name[i] + ".csv", encoding = 'gb2312')
    df['数据格式'] = ""
    #print(df.shape)
    for col in range(len(df)):
        if df.loc[col]["类型"] == "TN":
            df.loc[col]["数据格式"] = "tinyint"
        if df.loc[col]["类型"] == "TT":
            df.loc[col]["数据格式"] = "varchar(100)"
        if df.loc[col]["类型"] == "N":
            df.loc[col]["数据格式"] = "int"
        if df.loc[col]["类型"] == "ID":
            df.loc[col]["数据格式"] = "varchar(20)"
        if df.loc[col]["类型"] == "D":
            df.loc[col]["数据格式"] = "date"
        if df.loc[col]["类型"] == "F":
            df.loc[col]["数据格式"] = "float"
        if df.loc[col]["类型"] == "BB":
            df.loc[col]["数据格式"] = "blob"
        if df.loc[col]["类型"][0] == "C":
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
            sql =  df.iloc[col]["标识"].lower() + "  " +  df.iloc[col]["数据格式"] \
                +"  " + "COMMENT" + "  " + "\'"+ df.loc[col]["数据元名称"] +"\'" + ','
        print(sql)
    print(") COMMENT = '%s'" % (azbj_table_comment[i]))
    print('\n\n\n')




