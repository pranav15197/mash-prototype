from django.urls import path
from .views import RawVideoUploadView, InsertVideoTextView, AppView


urlpatterns = [
    path(r'app/', AppView.as_view()),
    path(r'insert_text/', InsertVideoTextView.as_view()),
    path(r'', RawVideoUploadView.as_view()),
]
