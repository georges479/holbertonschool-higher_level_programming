fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(resp => resp.json())
  .then(data => {
    const character = document.querySelector('#character');
    character.innerHTML = data.name;
  });