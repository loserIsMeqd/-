# 调用API文件夹里的tranfer文件夹里的ITK-SNAP 3.6文件夹里的itksnap-3.6.0-20170401-win64.exe文件

# import os
# os.system(r'API\tranfer\ITK-SNAP3.6\bin\ITK-SNAP.exe')

# 打开path变量里的文件夹
# import os
# path = r'API\tranfer\img_out'
# os.startfile(path)
# os.system(rz)

# 我想打开path的文件
# 关于django路径的问题，貌似html里的路径是相对于原来加上的 注意看游览器上的url地址
# 关于python路径的问题，路径的重定向功能的实现，不会再出现路径添加问题 https://blog.csdn.net/Ximerr/article/details/104720167
# 使用os.system调用python文件出现路径问题

# 打开exe文件
# os.system(r'API\tranfer\ITK-SNAP3.6\bin\ITK-SNAP.exe')


import os
# os.startfile(r'API\tranfer\ITK-SNAP3.6') # 打开文件夹
# os.system(r'API\tranfer\ITK-SNAP3.6\bin\ITK-SNAP.exe') # 打开exe文件
# 调用API文件中的uneKerasMaster文件夹中的predict.py文件 但是这个文件夹中的predict.py文件中的路径是相对路径 需要将工作目录切换到这个文件夹中
os.system(r'cd API\unetKerasMaster&&python predict.py') # 调用python文件

# os.system为子进程 不会影响主进程的实现
