window.onload = () => {
  console.log("page load");
  let video_chart;
  get_video_chart().then((data) => {
    video_chart = data;
    console.log(video_chart);
    change_youtube_player(video_chart["rank_1"]);
    set_video_chart(video_chart);
  });
};

async function get_video_chart() {
  let video_chart;

  let url = "api/video/chart";
  let response = await fetch(url)
    .then((response) => response.json())
    .then((data) => {
      video_chart = data;
    });

  return video_chart;
}

function change_youtube_player(video_id) {
  const player = document.getElementById("ytplayer");

  player.setAttribute("src", "https://www.youtube.com/embed/" + video_id);
}

function set_video_chart(video_chart) {
  document.getElementById("rank_1").textContent = video_chart["rank_1"];
  document.getElementById("rank_2").textContent = video_chart["rank_2"];
  document.getElementById("rank_3").textContent = video_chart["rank_3"];
  document.getElementById("rank_4").textContent = video_chart["rank_4"];
  document.getElementById("rank_5").textContent = video_chart["rank_5"];
}
