from django.urls import path

from video_app.views import (
    VideoChartView,
    VideoChartListView,
)

# video/
urlpatterns = [
    path("chart", VideoChartView.as_view(), name="chart"),
    path("chart/list", VideoChartListView.as_view(), name="chart_list"),
]
