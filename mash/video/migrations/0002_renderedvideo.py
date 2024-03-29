# Generated by Django 3.0 on 2019-12-15 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RenderedVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('raw_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.RawVideo')),
            ],
        ),
    ]
