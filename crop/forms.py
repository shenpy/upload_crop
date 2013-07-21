#coding=utf-8
from django import forms

class PhotoForm(forms.Form):
    photo_name = forms.ImageField()  #可选参数 label=u"图片"
     
class CutForm(forms.Form):
    x1=forms.IntegerField(widget=forms.TextInput(attrs={'size': 4,}))
    y1=forms.IntegerField(widget=forms.TextInput(attrs={'size': 4,}))
    x2=forms.IntegerField(widget=forms.TextInput(attrs={'size': 4,}))    
    y2=forms.IntegerField(widget=forms.TextInput(attrs={'size': 4,}))
    w=forms.IntegerField(widget=forms.TextInput(attrs={'size': 4,}))
    h=forms.IntegerField(widget=forms.TextInput(attrs={'size': 4,}))