from django.db import models


class RawVideo(models.Model):
    video = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.video.name
