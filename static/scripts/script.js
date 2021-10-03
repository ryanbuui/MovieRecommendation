function ratingPlus() {
  var rating = parseInt(document.getElementById("rating").value)
  if(rating < 5) {
    document.getElementById("rating").value = rating+1;
  }
}

function ratingMinus() {
  var rating = parseInt(document.getElementById("rating").value)
  if(rating > 0) {
    document.getElementById("rating").value = rating-1;
  }
}

function insertMovie(title) {
  document.getElementById("movieInput").value = title;
  document.getElementById("movieLabel").innerHTML = title;
}

function filterMovies() {
  input = document.getElementById("searchbar").value.toLowerCase();
  ul = document.getElementById("movieList");
  titles = document.getElementsByTagName('li');

  for(i = 0; i < titles.length; i++) {
    title = titles[i].innerHTML;

    if(title.toLowerCase().indexOf(input) > -1) {
      titles[i].style.display = "";
    } else {
      titles[i].style.display = "none";
    }

  }
}
