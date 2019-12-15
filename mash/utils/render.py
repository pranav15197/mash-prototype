from moviepy.editor import TextClip, CompositeVideoClip, VideoFileClip


def add_text_to_video(file_path, text):
    text_clip = TextClip(text, color='white', font="Amiri-Bold", fontsize=100).set_pos("center")
    clip = VideoFileClip(file_path)
    text_clip.duration = clip.duration
    final_clip = CompositeVideoClip([clip, text_clip])
    final_clip.duration = clip.duration
    final_clip.write_videofile("media/final_video.mp4")
