async function swCharacterName () {
  const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const character = await response.json();

  const parrafo = document.createElement('p');
  const text = document.createTextNode(character.name);
  parrafo.appendChild(text);
  document.querySelector('#character').appendChild(parrafo);
}
swCharacterName();
