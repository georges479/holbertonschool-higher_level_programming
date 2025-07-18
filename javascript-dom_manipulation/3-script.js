const toggle = document.querySelector('#toggle_header');
const header = document.querySelector('header');

if (!header.classList.contains('red') && !header.classList.contains('green')) {
  header.classList.add('red');
}

toggle.addEventListener('click', () => {
  if (header.classList.contains('red')) {
    header.classList.toggle('green');
  } else {
    header.classList.toggle('red');
  }
});