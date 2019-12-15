from .models import RawVideo, RenderedVideo


def get_video_by_id(video_id):
    return RawVideo.objects.get(pk=video_id)


def save_rendered_video(video, new_path):
    vid = RenderedVideo(raw_video=video)
    vid.video.name = new_path
    vid.save()
    return vid
