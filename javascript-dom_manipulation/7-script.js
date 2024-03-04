async function swCharacterName () {
  const response = await fetch('https://swapi-api.hbtn.io/api/films/?=json');
  const movies = await response.json();

  const films = movies.results;

  films.forEach(film => {
    const parrafo = document.createElement('li');
    const text = document.createTextNode(film.title);
    parrafo.appendChild(text);
    document.querySelector('#list_movies').appendChild(parrafo);
  });
}

swCharacterName();
