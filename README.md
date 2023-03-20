# python_parse_fio
python脚本解析fio的结果，提出IOPS和带宽，结果输出到CSV文件中  
  
步骤：  
  1.在test_fio.sh更改相对应的fio参数  
  2.后台运行脚本，结果重定向到txt文件：nohup ./test_fio.sh >> read.txt 2>&1 &  
  3.解释脚本：python_parse_fio.py  
