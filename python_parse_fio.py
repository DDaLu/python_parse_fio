import csv
import os
 
'''
fio结果 解决python来解析的问题
批量解决fio生成问题
'''
def fiodata_write_to_csv(outfilepath, file, data_of_file):
    '''
    将截取好的数据写入csv文件
    :param outfilepath: 输出目录
    :param file: 文件名
    :param data_of_file:截取好的数据
    :return: 无
    '''
    with open(outfilepath + '/' + file + '.csv', 'w', encoding='utf8', newline='') as r:
        csv_writer = csv.writer(r)
        # 写入表头
        Data = []
        csvfile_head = ['fromate', 'IOPS', 'BW']
        Data.append(csvfile_head)
        Data.extend(data_of_file)
        Data = zip(*Data)
        # csv_writer.writerow(csvfile_head)
        # 写入所有文件提取的数据
        csv_writer.writerows(Data)
        r.close()
    pass
 
 
def get_data(inputfilepath):
    '''
    从fio文件中截取数据
    :param inputfilepath:文件路径
    :return: 截取好的数据
    '''
    data_of_file = []
    with open(inputfilepath, "r") as f:
        for line in f.readlines():
            if "rw=" in line or "read:" in line or 'write:' in line:
                # print("line:"+line)
                if "bs=" in line:
                    cut_index = line.find("bs=")
                    # print(cut_index)
                    fio_fromate = line[16:cut_index-2]
                    # print("fio_fromate:"+fio_fromate)
                    # data_of_file.append([fio_fromate])
                if "read:" in line or 'write:' in line:
                    cut_index2 = line.find("MB/s")
                    cut_index3 = line.find(":")
                    cut_index4 = line.find("IOPS=")
                    cut_index5 = line.find(",")
                    cut_index6 = line.find(" (")
                    read_or_write = line[1:cut_index3]
                    data_IOPS = line[cut_index4 + 5:cut_index5]
                    data_BW = line[cut_index6 + 2:cut_index2]
 
                    data_of_file.append([fio_fromate, data_IOPS, data_BW])
        print("fio数据提取成功")
    # for i in data_of_file:
    #     print(i)
    # data_of_file = zip(*data_of_file)
    return data_of_file
 
 
def fiofilePath_read(inputfilePath, outfilepath):
    '''
    批量数据生成
    :param inputfilePath:文件路径
    :return: 无
    '''
    rightCount = 0
    errorCount = 0
 
    # 修改目录方式下划线方法
    inputfilePath = inputfilePath.replace('\\', '/')
    # outfilepath = r"E:\zresult"
    for file in os.listdir(inputfilePath):
        try:
            if str(file[-3:]) == "txt":
                print(file)
                data_of_file = get_data(inputfilePath + '/' + file)
                print(data_of_file)
                fiodata_write_to_csv(outfilepath, file, data_of_file)
                print(file + '文件提取完成')
                rightCount += 1
        except:
            print(file + '文件提取------失败')
            errorCount += 1
    print('\n', '文件提取完成 ', rightCount, '个文件成功', errorCount, '个文件有误')
    print("提取总结文件目录：", outfilepath)
    # 打开窗口
    # os.startfile(outfilepath)
 
 
if __name__ == '__main__':
    # 输入目录
    inputfilePath = r"G:\python"
    # 输出目录
    outfilepath = r"G:\python"
    # outfilepath = r"E:\\"
    fiofilePath_read(inputfilePath, outfilepath)