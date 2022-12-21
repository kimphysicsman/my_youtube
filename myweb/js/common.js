window.onload = () => {
  let video_chart;
  let chart_list;

  get_video_chart().then((data) => {
    video_chart = data;
    change_youtube_player(video_chart[0]["id"]);
    set_video_chart(video_chart);
  });

  get_chart_list().then((data) => {
    chart_list = data;
    console.log(chart_list);
    set_chart_list(chart_list);
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
  const player = document.getElementById("ytplayer");

  document.getElementById("rank_1").textContent = video_chart[0]["title"];
  document.getElementById("rank_2").textContent = video_chart[1]["title"];
  document.getElementById("rank_3").textContent = video_chart[2]["title"];
  document.getElementById("rank_4").textContent = video_chart[3]["title"];
  document.getElementById("rank_5").textContent = video_chart[4]["title"];

  document.getElementById("rank_1").addEventListener("click", () => {
    player.setAttribute(
      "src",
      "https://www.youtube.com/embed/" + video_chart[0]["id"]
    );
  });

  document.getElementById("rank_2").addEventListener("click", () => {
    player.setAttribute(
      "src",
      "https://www.youtube.com/embed/" + video_chart[1]["id"]
    );
  });

  document.getElementById("rank_3").addEventListener("click", () => {
    player.setAttribute(
      "src",
      "https://www.youtube.com/embed/" + video_chart[2]["id"]
    );
  });

  document.getElementById("rank_4").addEventListener("click", () => {
    player.setAttribute(
      "src",
      "https://www.youtube.com/embed/" + video_chart[3]["id"]
    );
  });

  document.getElementById("rank_5").addEventListener("click", () => {
    player.setAttribute(
      "src",
      "https://www.youtube.com/embed/" + video_chart[4]["id"]
    );
  });
}

async function get_chart_list() {
  let chart_list;

  const url = "api/video/chart/list";
  const response = await fetch(url)
    .then((response) => response.json())
    .then((data) => {
      chart_list = data;
    });

  return chart_list;
}

function set_chart_list(chart_list) {
  for (let i = 0; i < chart_list.length; i++) {
    document.getElementById(
      "chart_" + (i + 1).toString() + "_date"
    ).textContent = chart_list[i]["date"];

    for (let j = 0; j < 5; j++) {
      title = chart_list[i]["rank_" + (j + 1).toString() + "_title"];
      if (!title) title = chart_list[i]["rank_" + (j + 1).toString()];

      document.getElementById(
        "chart_" + (i + 1).toString() + "_" + (j + 1).toString()
      ).textContent = title;
    }
  }
}
