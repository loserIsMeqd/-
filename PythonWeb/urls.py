from django.contrib import admin
from django.urls import path
from . import views
# 导入database应用下的views.py文件
import database.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('openfolder/', views.openfolder),
    path('predict/', views.predict),
    path('getfile/', views.getfile),
    path('openexe/', views.openexe),
    path('opentrainfile/', views.opentrainfile),
    # path('train/', views.train),
    path('logs/', views.logs),
    path('add/', database.views.add),
]
