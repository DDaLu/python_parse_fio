# python_parse_fio
python脚本解析fio的结果，提取fio的IOPS和带宽，输出到CSV文件中  
  
步骤：  
  1.在test_fio.sh更改相对应的fio参数  
  2.后台运行脚本，结果重定向到txt文件：nohup ./test_fio.sh >> read.txt 2>&1 &  
  3.解释脚本：python_parse_fio.py  
![image](https://user-images.githubusercontent.com/49317776/226300937-f7b85d75-fc27-442f-87af-b08dd25d331b.png)
