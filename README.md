# AutoCreateTable
根据《数据采集标准》中的表格式自动生成SQL语句

## 准备工作
将《数据采集标准》中的每个表的数据元名称、标识、类型字段导出到csv文件，命名为首拼小写，例如安置帮教管制信息表命名为azbj_gzxxb.csv


## 生成SQL语句
shell: python CreateSQL.py --tbname azbj_gzxxb --comment "管制信息表" --csvfile azbj_gzxxb.csv




