from django.shortcuts import render
from django.http import HttpResponse
from .models import PrimaryDate

# Create your views here.
import sqlite3
import os

# 添加数据记录
def add(request):
    if request.method == "GET":
        # name = request.POST.get("name")
        # age = request.POST.get("age")
        # disease = request.POST.get("disease")

        # 先测试
        name = "test"
        age = 20
        disease = "test"

        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()
        sql = "insert into database_primarydate(name,age,disease) values('%s','%s','%s')" % (name, age, disease)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

        # 利用orm添加数据
        PrimaryDate.objects.create(name=name, age=age, disease=disease)


        return HttpResponse("添加成功")
    else:
        return HttpResponse("添加失败")