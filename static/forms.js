const input = document.querySelector('.form-group input');
const label = document.querySelector('.form-group label');

input.addEventListener('input', () => {
  if (input.value.trim() !== '') {
    label.classList.add('floating');
  } else {
    label.classList.remove('floating');
  }
});