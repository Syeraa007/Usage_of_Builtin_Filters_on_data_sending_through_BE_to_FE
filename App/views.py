from django.shortcuts import render

# Create your views here.
import datetime
def buitlin_filters(request):
    dates=datetime.datetime.now()
    d={'data':'ThiS is WEEkenD  NoW we HaVe MoCK ShootING','count':10,'dates':dates,'mine':'hiihii how are You daRinliG'}
    return render(request,'buitlin_filters.html',d)