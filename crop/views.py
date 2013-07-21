	

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.contrib import messages
import os, uuid, ImageFile, Image

from crop.forms import PhotoForm, CutForm
from crop.models import Photo

from UpFile.settings import MEDIA_ROOT,CROP_ABS_PATH,CROP_VIR_PATH

def index(request, templates="crop/index.html"): 
#默认在当前app所在文件夹下的templates文件夹寻找crop/index.html
    template_var={}
    form=PhotoForm()       #生成表单(包含图片标签 input  name='photo_name')
    if request.method=="POST":
        form = PhotoForm(request.POST.copy(),request.FILES)
        if form.is_valid():
            file=request.FILES.get("photo_name",None)
            if file:
                p=ImageFile.Parser()
                for c in file.chunks():
                    p.feed(c)
                img=p.close()
                
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
                if img.size[0]>img.size[1]:  # w=img.size[0] h=img.size[1]
                    offset=int(img.size[0]-img.size[1])/2
                  #  img=img.crop((offset,0,int(img.size[0]-offset),img.size[1]))
                else:
                    offset=int(img.size[1]-img.size[0])/2
                   # img=img.crop((0,offset,img.size[0],(img.size[1]-offset)))
                #img.thumbnail((300, 300))
                
                file_name="ledapei_%s_origin.jpg"%str(uuid.uuid1())    #命名图片
                img.save(os.path.join(CROP_ABS_PATH,file_name),"JPEG",quality=100)
                messages.info(request,  "上传成功")
                p=Photo.objects.create(photo_name=file_name)
                p.save()
                return HttpResponseRedirect(reverse('crop:crop_cut',kwargs={"id":p.id}))
                
    template_var["form"] = form
    return render_to_response(templates, template_var, context_instance=RequestContext(request))

	
def cut(request, id, templates="crop/cut.html"):
    template_var={}
    p=get_object_or_404(Photo,pk=int(id))
        
    if not p.photo_name:
        messages.info(request, "请先上传图片！")
        return HttpResponseRedirect(reverse('crop:crop_index'))
        
    template_var["vir_path"]=os.path.join(CROP_VIR_PATH,p.photo_name)    
    
    form=CutForm()
    if request.method=='POST':
        form=CutForm(request.POST)
        if form.is_valid():            
            try:
                img=Image.open(os.path.join(CROP_ABS_PATH, p.photo_name))                
            except IOError:
                messages.info(request, "读取文件错误！")
                
            data=form.cleaned_data
            img=img.crop((data["x1"],data["y1"],data["x2"],data["y2"]))
            img.thumbnail((800, 800))  #如果crop后图片尺寸大于800，将裁成800，小于800的没变化
            file_name="%s_%s"%(os.path.splitext(p.photo_name)[0],"_crop.jpg")            
            img.save(os.path.join(CROP_ABS_PATH, file_name),"JPEG",quality=100)
            
            p.photo_thumb=file_name
            p.save()
                     
            messages.info(request, "剪切成功！")
            return HttpResponseRedirect(reverse('crop:crop_show'))
        else:
            messages.info(request, "请剪切后 再保存！")
    template_var["form"]=form
    return render_to_response(templates,template_var,context_instance=RequestContext(request))


def show(request,templates="crop/show.html"):
    template_var={}
    photos=Photo.objects.all()
    template_var["path"]=CROP_VIR_PATH
    template_var["photos"]=photos
    return render_to_response(templates,template_var,context_instance=RequestContext(request))