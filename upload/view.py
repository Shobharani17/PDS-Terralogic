from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Upload_files
import os
from jsonfile import settings


def home(request):
        context={'file':Upload_files.objects.all()}
        return render (request,'/upload/templates/index.html/',context)

def download (request,path):
        file_path=os.path.join(settings.MEDIA_ROOT,path)
        if os.path.exists(file_path):
            with open(file_path,'rb') as fh:
                response=HttpResponse(fh.read(),content_type="application/files")
                response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
                return response
        raise Http404