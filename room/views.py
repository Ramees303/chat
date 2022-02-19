from django.shortcuts import render
from .models import Room,Message
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def rooms(request):
    room=Room.objects.all()
    
    return render(request,'room/rooms.html',{'room':room})

@login_required
def roomdetail(request,slug):
    rooms=Room.objects.get(slug=slug)
    messages=Message.objects.filter(room=rooms)[0:20]
    # getting msg from room and slicing it
    return render(request,'room/roomdetail.html',{'rooms':rooms,'messages':messages})