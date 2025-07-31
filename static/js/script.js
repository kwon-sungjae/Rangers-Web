const artists = [
  {
    name: "윤철식",
    image: "images/team-1.jpg",
    link: "#",
  },
  {
    name: "이예지",
    image: "images/team-2.jpg",
    link: "#",
  },
  {
    name: "강혜정",
    image: "images/team-3.jpg",
    link: "#",
  },
  {
    name: "이준희",
    image: "images/team-4.jpg",
    link: "#",
  },
  {
    name: "권성재",
    image: "images/team-5.jpg",
    link: "#",
  },
];
const list = document.getElementById("list");

function showArtists(query) {
  list.innerHTML = "";

  const filteredArtists = artists.filter((artist) =>
    artist.name.includes(query)
  );

  filteredArtists.forEach((artist) => {
    const col = document.createElement("div");
    col.className = "col-md-3 ftco-animate";
    const agent = document.createElement("div");
    agent.className = "agent";
    const img = document.createElement("img");
    img.src = artist.image;
    img.className = "img-fluid";
    img.alt = "Colorlib Template";
    const desc = document.createElement("div");
    desc.className = "desc";
    const h3 = document.createElement("h3");
    const a = document.createElement("a");
    a.href = artist.link;
    a.innerHTML = artist.name;
    h3.appendChild(a);
    const p = document.createElement("p");
    p.className = "h-info";
    const aLocation = document.createElement("a");
    aLocation.href = artist.link;
    aLocation.className = "location";
    aLocation.innerHTML = "채팅하러 가기";
    p.appendChild(aLocation);

    desc.appendChild(h3);
    desc.appendChild(p);
    agent.appendChild(img);
    agent.appendChild(desc);
    col.appendChild(agent);
    list.appendChild(col);
  });
}

const searchInput = document.getElementById("searchInput");
const searchButton = document.querySelector(".search-location button");

function handleSearch(event) {
  event.preventDefault();
  const query = searchInput.value.trim().toLowerCase();
  showArtists(query);
}

searchButton.addEventListener("click", handleSearch);
searchInput.addEventListener("input", handleSearch);

// 초기화면에 모든 아티스트 보여주기
showArtists("");
