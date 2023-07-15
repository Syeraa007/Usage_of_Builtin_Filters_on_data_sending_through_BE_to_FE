from django.shortcuts import render

# Create your views here.
import datetime
def buitlin_filters(request):
    dates=datetime.datetime.now()
    d={'data':'THIS is WEEkenD  NoW we HaVe MoCK ShootING','count':12,'dates':dates}
    return render(request,'buitlin_filters.html',d)