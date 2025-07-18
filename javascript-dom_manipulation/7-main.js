const movieListElem = document.querySelector('#list_movies');

function addMovieToList (title) {
  const newMovie = document.createElement('li');
  newMovie.innerText = title;
  movieListElem.append(newMovie);
}

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(resp => resp.json())
  .then(data => {
    for (movie of data.results) {
      addMovieToList(movie.title);
    }
  });