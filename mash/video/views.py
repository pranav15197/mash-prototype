from django.views.generic import TemplateView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from utils.render import add_text_to_video
from .services import get_video_by_id, save_rendered_video
from .serializers import RawVideoSerializer, InsertTextInputSerializer, RenderedVideoSerializer


class RawVideoUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = RawVideoSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InsertVideoTextView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = InsertTextInputSerializer(data=request.data)
        if serializer.is_valid():
            video_id, text, position = [serializer.data[k] for k in ['raw_video_id', 'text', 'position']]
            raw_video = get_video_by_id(video_id)
            rendered_file_path = add_text_to_video(raw_video, text, position)
            rendered_video = save_rendered_video(raw_video, rendered_file_path)
            serializer = RenderedVideoSerializer(rendered_video)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppView(TemplateView):
    template_name = "video/app.html"
