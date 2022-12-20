import requests
import os

from video_app.serializers import ChartModelSerializer
from video_app.models import ChartModel

YOUTUBE_VIDEO_API_URL = "https://www.googleapis.com/youtube/v3/videos"
API_KEY = os.environ.get("API_KEY")

def get_video_chart_most_popular():
    """인기차트 조회 기능 (5개)

    Returns:
        list: 인기 동영상 id 리스트
    """

    # api_url = YOUTUBE_VIDEO_API_URL + f"?part=id&chart=mostPopular&key={API_KEY}"
    # response = requests.get(api_url)
    # response_json = response.json()

    # items = response_json["items"]
    # item_ids = [item["id"] for item in items]

    # return item_ids

    return {
        "rank_1" : "Mxkg3qLIPC8",
        "rank_2" : "Z8mOxhAjyqQ",
        "rank_3" : "HkvQywg_uZA",
        "rank_4" : "-lsFs2615gw",
        "rank_5" : "bK6ldnjE3Y0"
    }

def save_video_chart(video_chart):

    try:
        serializer = ChartModelSerializer(data=video_chart)
        
        if serializer.is_valid():
            serializer.save()

        return serializer.data
   
    except:
        return None


def get_video_chart_list():
    chart_list = ChartModel.objects.all()

    serializer = ChartModelSerializer(chart_list, many=True)
    return serializer.data
