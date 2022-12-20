window.onload = () => {
  console.log("page load");
  get_video_chart();
};

async function get_video_chart() {
  let video_chart;

  let url = "api/video/chart";
  let response = await fetch(url)
    .then((response) => response.json())
    .then((data) => {
      video_chart = data;
      console.log(video_chart);
    });
}
