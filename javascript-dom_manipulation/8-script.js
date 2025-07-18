const helloIdElem = document.querySelector('#hello');

const options = {
  mode: 'no-cors'
};

fetch('https://fourtonfish.com/hellosalut/?lang=fr', options)
  .then(resp => resp.json())
  .then(data => {
    helloIdElem.innerHTML = data.hello;
  })
  .catch(err => console.log(err));