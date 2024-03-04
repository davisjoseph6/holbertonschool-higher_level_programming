document.querySelector('#add_item').onclick = function () {
  const element = document.createElement('li');
  const text = document.createTextNode('item');
  element.appendChild(text);
  document.querySelector('.my_list').appendChild(element);
};
