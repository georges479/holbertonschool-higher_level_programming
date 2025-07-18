const addItem = document.querySelector('#add_item');

addItem.addEventListener('click', () => {
  const newListItem = document.createElement('li');
  newListItem.innerText = 'Item';
  const list = document.querySelector('ul.my_list');
  list.append(newListItem);
});