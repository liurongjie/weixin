from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [
    path('justtry', views.justtry, name='尝试'),
    path('login', views.login, name='登陆'),
    path('verify', views.verify, name='实名认证'),
    path('home', views.home, name='首页'),
    path('firstcomment', views.firstcomment, name='首页评论'),
    path('scancomment', views.scancomment, name='浏览评论'),
    path('getperiod', views.getperiod, name='获取订单信息'),
    path('orderlist', views.orderlist, name='订单信息'),
    path('orderdetail', views.orderdetail, name='订单信息'),
    path('cancel', views.cancel, name='取消'),
    path('completeorder', views.completeorder, name='订单完成'),
    path('comment', views.comment, name='评论'),
    path('buyalone', views.buyalone, name='购买'),
    path('buytogether', views.buytogether, name='购买'),
    path('need', views.need, name='购买'),
    path('cutprice', views.cutprice, name='我要砍价'),
    path('sign', views.sign, name='签到'),
    path('getgift', views.getgift, name='抽奖'),
    path('accountdetail', views.accountdetail, name='贝壳明细'),


]