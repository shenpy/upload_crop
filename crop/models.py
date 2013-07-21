#coding=utf-8
from django.db import models

class Photo(models.Model):
    photo_name=models.CharField(u"图片路径",max_length=255)
    photo_thumb=models.CharField(u"图片缩略图",max_length=255)
    
    
