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

    # api_url = YOUTUBE_VIDEO_API_URL + f"?part=snippet&chart=mostPopular&regionCode=KR&key={API_KEY}"
    # response = requests.get(api_url)
    # response_json = response.json()

    # items = response_json["items"]
    # item_info_list = []
    # for item in items:
    #     item_info = {
    #         "id": item["id"],
    #         "title": item["snippet"]["title"]
    #     }
    #     item_info_list.append(item_info)

    # return item_info_list

    return [
        {"id":"pSUydWEqKwE", "title": "NewJeans (뉴진스) 'Ditto' Official MV (side A)"},
        {"id": "V37TaRdVUQY", "title": "NewJeans (뉴진스) 'Ditto' Official MV (side B)"},
        {"id": "gvLz7ZIv6gs", "title":"[안정환의 말말말] 메시와 안느의 '라스트 댄스'✨ㅣ2022 카타르월드컵 결승전 아르헨티나 vs 프랑스"},
        {"id": "zGsqGy5fZ8s", "title":"[님아 그 시장을 가오_EP. 18_속초] “사장님 국수는 어디 갔어요?” 국수 찾는 데 한참 걸렸습니다! 회 먹다 식사 끝나는 희한한 회국수집!"},
        {"id": "caBouLh_vto", "title":"1++ 한우를 맛 본 프나르의 이상한 반응, 그리고 가족과의 첫만남 - 국내 (1)"},
    ]

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
