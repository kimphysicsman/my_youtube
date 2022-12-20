from django.urls import reverse

from rest_framework.test import APITestCase

from video_app.models import ChartModel

class TestVideoChartView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        temp = {
            "rank_1": "test_1",
            "rank_2": "test_2",
            "rank_3": "test_3",
            "rank_4": "test_4",
            "rank_5": "test_5"
            }

        ChartModel.objects.create(**temp)
        ChartModel.objects.create(**temp)
        ChartModel.objects.create(**temp)        


    def test_get_video_chart_view(self):

        response = self.client.get(
            reverse("chart"), 
        )
        print(response.data)

    def test_save_chart(self):

        request_data = {
            "rank_1": "a",
            "rank_2": "b",
            "rank_3": "c",
            "rank_4": "d",
            "rank_5": "e"
        }

        response = self.client.post(
            reverse("chart"),
            request_data,
            format='json'
        )

        print(response.data)

    def test_get_chart_list(self):

        response = self.client.get(
            reverse("chart_list"), 
        )

        for data in response.data:
            print(data)