import os
import numpy as np
import nibabel as nib
import imageio
import matplotlib
from nibabel.viewers import OrthoSlicer3D
from matplotlib import pylab as plt

# 将数据先保存到一个文件夹中
def read_niifile(niifilepath):  # 读取niifile文件
    img = nib.load(niifilepath)  # 下载niifile文件（其实是提取文件）
    img_fdata = img.get_fdata()  # 获取niifile数据
    return img_fdata


def save_fig(niifilepath, savepath):  # 保存为图片
    fdata = read_niifile(niifilepath)  # 调用上面的函数，获得数据
    (x, y, z) = fdata.shape  # 获得数据shape信息：（长，宽，维度-切片数量，第四维）
    b = np.zeros((536, 536))
    all = []
    num=0
    a=0
    for k in range(x):
        silce = fdata[:, :, k]  # 三个位置表示三个不同角度的切片
        # labels
        if np.all(silce == 0):
            a = a + 1
        else:
            all.append(k)
            num=num+1
            imageio.imwrite(os.path.join(savepath, 'qian_{}.png'.format(k)), silce)
    # #     # image
    #     if k>=157 and k<=203:
    #         a = a + 1
    #         imageio.imwrite(os.path.join(savepath, 'qian_{}.png'.format(k)), silce)
    #     # 将切片信息保存为png格式
    print(num)
    print(x)


if __name__ == '__main__':
    niifilepath = 'D:\\hospital_data_throat\\Q_Y_throat_data_patient\\data\\new_data\\zrl_data\\image\\Array_0000158260.nii.gz'
    savepath = 'D:\\hospital_data_throat\\Q_Y_throat_data_patient\\data\\Array_0000158260'
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    save_fig(niifilepath, savepath)