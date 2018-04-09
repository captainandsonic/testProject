# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models
# Create your views here.

# user_list = [
#     {"user":"111", "pwd":"p111"},
#     {"user":"222", "pwd":"p222"},
# ]


def index(request):
    #request.POST
    #request.GET
    #return HttpResponse("hello, world!!!")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # print (username,password)
        # temp = {"user":username, "pwd":password}
        # user_list.append(temp)
        models.UserInfo.objects.create(user=username,pwd=password)
    user_list = models.UserInfo.objects.all()

    return render(request, "cmdb/index.html", {"data":user_list})