from django.shortcuts import render
from django.http import HttpResponseRedirect

from DgRun.models import RelayData


def delete_all(request):
    RelayData.objects.all().delete()
    return HttpResponseRedirect('/admin')
