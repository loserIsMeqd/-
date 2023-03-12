# https://blog.csdn.net/weixin_48780159/article/details/125432431 参考这篇文章
from PIL import Image
import numpy as np
import SimpleITK as sitk
import os
png_path='img_out'
nii_path='nii/'
# nii_file = sitk.GetImageFromArray(anno_mat)
# # anno_mat 为一个矩阵，其维度必须是按照(样本数*高度*宽度)排列 否则，保存的结果错误
# sitk.WriteImage(nii_file, nii_path)  # nii_path 为保存路径

empt_mat = []
files=os.listdir(png_path)
files.sort()
for i in files:
    if i!='.DS_Store':
        print(i)

        img1 = Image.open(os.path.join(png_path,i))
        img2 = np.array(img1)
        # print(img2)
    # 这里取png图片的前三个通道，去除第四个透明通道 方便后续的nii文件的处理
        empt_mat.append(img2)
        print(empt_mat)
        print(len(empt_mat))
        emp = np.array(empt_mat)
        # print(emp)
        nii_file = sitk.GetImageFromArray(emp)
        # print(111)
        # print(nii_file)
    # 此处的emp的格式为样本数*高度*宽度*通道数
    # 不要颠倒这些维度的顺序，否则文件保存错误
nii_path=(nii_path+'NIItoPNGzhou'+'.nii.gz')
sitk.WriteImage(nii_file, nii_path)  # nii_path 为保存路径