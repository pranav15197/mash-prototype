from django.db import models


class RawVideo(models.Model):
    video = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.video.name


class RenderedVideo(models.Model):
    raw_video = models.ForeignKey("RawVideo", on_delete=models.CASCADE)
    video = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.video.name
