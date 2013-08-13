from django.shortcuts import render
from django.conf import settings


def index(request):
    custom_setting = settings.CUSTOM_SETTING
    text = 'Hello world'
    return render(request, 'rename_this_app/index.html', locals())
