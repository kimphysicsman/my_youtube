from django.urls import path

from video_app.views import VideoChartView

# video/
urlpatterns = [
    path("", VideoChartView.as_view(), name="video"),
]
