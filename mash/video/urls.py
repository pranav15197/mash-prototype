from django.urls import path
from .views import RawVideoUploadView, InsertVideoTextView


urlpatterns = [
    path(r'insert_text/', InsertVideoTextView.as_view()),
    path(r'', RawVideoUploadView.as_view()),
]
