from django.shortcuts import render, get_object_or_404


from .models import Video


def index(request):
    return render(request, 'index.html')

def video(request):
    videos = Video.objects.all()
    return render(request, 'video.html', {'videos': videos})

def video_detail(request, pk):
    video = get_object_or_404(Video, id=pk)
    return render(request, 'video-lesson.html', {'video':video})
