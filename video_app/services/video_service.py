import requests
import os

from video_app.serializers import ChartModelSerializer
from video_app.models import ChartModel

YOUTUBE_VIDEO_API_URL = "https://www.googleapis.com/youtube/v3/videos"
API_KEY = os.environ.get("API_KEY")

def get_video_chart_most_popular():
    """인기차트 조회 기능 (5개)

    Returns:
        list: 인기 동영상 리스트
    """

    api_url = YOUTUBE_VIDEO_API_URL + f"?part=snippet&chart=mostPopular&regionCode=KR&key={API_KEY}"
    response = requests.get(api_url)
    response_json = response.json()

    items = response_json["items"]
    item_info_list = []
    for item in items:
        item_info = {
            "id": item["id"],
            "title": item["snippet"]["title"]
        }
        item_info_list.append(item_info)

    return item_info_list



def save_video_chart(video_chart):

    try:
        serializer = ChartModelSerializer(data=video_chart)
        
        if serializer.is_valid():
            serializer.save()

        return serializer.data
   
    except:
        return None


def get_video_chart_list():
    chart_list = ChartModel.objects.all().order_by("date").reverse()[:4]

    serializer = ChartModelSerializer(chart_list, many=True)
    return serializer.data
