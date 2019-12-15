import datetime
import os
from moviepy.editor import TextClip, CompositeVideoClip, VideoFileClip


def add_text_to_video(video, text):
    datetime.datetime.utctimetuple
    file_path = video.video.path
    text_clip = TextClip(text, color='white', font="Amiri-Bold", fontsize=100).set_pos("center")
    clip = VideoFileClip(file_path)
    text_clip.duration = clip.duration
    final_clip = CompositeVideoClip([clip, text_clip])
    final_clip.duration = clip.duration
    orig_name, ext = os.path.splitext(video.video.name)
    new_name = "%s_%d%s" % (orig_name, datetime.datetime.now().timestamp(), ext)
    final_clip.write_videofile("media/" + new_name)
    return new_name
