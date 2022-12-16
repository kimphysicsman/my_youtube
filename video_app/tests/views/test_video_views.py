from django.urls import reverse


from rest_framework.test import APITestCase


class TestVideoChartView(APITestCase):

    def test_get_video_chart_view(self):

        response = self.client.get(
            reverse("video"), 
        )
        print(response.data)