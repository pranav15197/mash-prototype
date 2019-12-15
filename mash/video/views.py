from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from utils.render import add_text_to_video
from .services import get_video_path_by_id
from .serializers import RawVideoSerializer, InsertTextInputSerializer


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
            video_id, text = [serializer.data[k] for k in ['raw_video_id', 'text']]
            file_path = get_video_path_by_id(video_id)
            add_text_to_video(file_path, text)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
