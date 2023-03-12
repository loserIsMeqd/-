from django.shortcuts import render
# 实现转向首页功能
from django.http import HttpResponseRedirect
import os
 
def index(request):
    return render(request, 'index.html')

def openfolder(request):
    path = r'API\unetKerasMaster\img'
    os.startfile(path)
    return HttpResponseRedirect('/')

def predict(request):
    # 暂时改变路径
    os.system(r'cd API\unetKerasMaster&&python predict.py')
    os.system(r'cd API\unetKerasMaster&&python pngToNii.py')
    return HttpResponseRedirect('/')

def getfile(request):
    path = r'API\unetKerasMaster\img_out'
    os.startfile(path)
    os.startfile(r'API\unetKerasMaster\nii')
    return HttpResponseRedirect('/')

def openexe(request):
    os.system(r'API\tranfer\ITK-SNAP3.6\bin\ITK-SNAP.exe')
    return HttpResponseRedirect('/')

def opentrainfile(request):
    path = r'API\unetKerasMaster\VOCdevkit\VOC2007\JPEGImages'
    os.startfile(path)
    path = r'API\unetKerasMaster\VOCdevkit\VOC2007\SegmentationClass'
    os.startfile(path)
    return HttpResponseRedirect('/')

def train(request):
    os.system(r'cd API\unetKerasMaster&&python train.py')
    return HttpResponseRedirect('/')

def logs(request):
    path = r'API\unetKerasMaster\logs'
    os.startfile(path)
    return HttpResponseRedirect('/')


    
