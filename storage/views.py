# -*- coding: utf-8 -*-

# Create your views here.
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max

from storage.forms import UploadFileForm, FileGetterForm
from storage.models import Picture

from datetime import datetime

import urllib

def main_page(request):
#    output = '''
#        <html>
#        <head><title>%s</title></head>
#        <body>
#            <h1>%s</h1>
#        </body>
#        </html>
#    ''' % (
#           '장고|Framework',
#           '장고 Framework에 오신 것을 환영합니다.'
#           )
#    return HttpResponse (output)
    return render_to_response('hello.html', None)



def ls(request):
    pics = Picture.objects.all().order_by('-created')
    ctx = RequestContext(request, {'pictures': pics})
    
    return render_to_response('list.html', ctx)



@csrf_exempt
def poster(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file_uploaded'])
            return HttpResponseRedirect('/upload_success/')
    else:
        form = UploadFileForm()
        return render_to_response('upload.html', {'form': form})


def upload_success(request):
    return render_to_response('upload_success.html', None)



def handle_uploaded_file(f):
    max_file_id = Picture.objects.all().aggregate(Max('file_id'))['file_id__max']
    
    if max_file_id == None:
        max_file_id = 0
        
    max_file_id = max_file_id + 1
    
    new_picture = Picture(file_id = max_file_id,
                          user_id = 'anonymous',
                          created = datetime.now(),
                          favorite = 'no',
                          simple_name = f.name,
                          size = f.size
                          )
    new_picture.save()
    
    up_file_path = r'c:\temp\%s'
    
    up_file = open(up_file_path %(max_file_id) , 'wb+')
    #for chunk in f.chunks():
    for ck in f:
        up_file.write(ck)
        
    up_file.close()
    

def preview(request):
    id = int(request.GET['file_id'])
    print 'id ------------------> ' + str(id)
    #pics = Picture.objects.get(file_id=id)
    pics = Picture.objects.all().filter(file_id=id)
    ctx = RequestContext(request, {'pictures': pics})
    return render_to_response('view.html', ctx)


def getter(request):
    id = int(request.GET['file_id'])
    print 'id ------------------> ' + str(id)
    pics = Picture.objects.get(file_id=id)
    
    up_file_path = r'c:\temp\%s'
    down_file_path = r'd:\temp\%s'
    
    f_name = pics.simple_name
    f_size = pics.size
    
    f = open(up_file_path %(str(id)), 'rb')
    
    down_file = open(down_file_path %(f_name), 'wb+')
    for wf in f:
        down_file.write(wf)
    
    down_file.close()
    f.close()
    
    #html = "<html><body></body></html>"
    #return HttpResponse(html)
    return render_to_response('download_success.html', None)
    