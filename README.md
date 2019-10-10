# AutoCreateTable
根据《数据采集标准》中的表格式自动生成SQL语句

## 准备工作
1.将《数据采集标准》中的数据元名称、标识、类型字段导出到csv文件，命名为首拼小写，如azbj_bffaxxb.csv
2.建立表名与中文注释的字典:create_table_dic = {azbj_bffaxxb : "帮扶方案信息采集表"}

## 生成SQL语句
shell: python CreateSQL.py azbj_bffaxxb 


