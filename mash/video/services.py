from .models import RawVideo


def get_video_path_by_id(video_id):
    return RawVideo.objects.get(pk=video_id).video.path
