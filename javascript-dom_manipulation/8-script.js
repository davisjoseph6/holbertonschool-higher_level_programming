async function fetchHello () {
  const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
  const hello = await response.json();

  const hi = document.createElement('p');
  const text = document.createTextNode(hello.hello);
  hi.appendChild(text);
  document.querySelector('#hello').appendChild(hi);
  console.log(hello.hello);
}

fetchHello();
