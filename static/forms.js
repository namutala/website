const formGroupInputs = document.querySelectorAll('.form-group input');

formGroupInputs.forEach(input => {
  const label = input.nextElementSibling; // Assuming label is the next sibling

  input.addEventListener('input', () => {
    if (input.value.trim() !== '') {
      label.classList.add('floating');
    } 
  });

  if (input.value.trim() !== '') {
    label.classList.add('floating');
  } 
});
