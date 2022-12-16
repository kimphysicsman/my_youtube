import requests
import os

YOUTUBE_VIDEO_API_URL = "https://www.googleapis.com/youtube/v3/videos"
API_KEY = os.environ.get("API_KEY")

def get_video_chart_most_popular():
    """인기차트 조회 기능 (5개)

    Returns:
        list: 인기 동영상 id 리스트
    """

    api_url = YOUTUBE_VIDEO_API_URL + f"?part=id&chart=mostPopular&key={API_KEY}"
    response = requests.get(api_url)
    response_json = response.json()

    items = response_json["items"]
    item_ids = [item["id"] for item in items]

    return item_ids