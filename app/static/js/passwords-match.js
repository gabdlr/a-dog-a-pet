(() => {
  'use strict'
  const password = document.getElementById("password");
  const password_validation = document.getElementById("password-confirmation");
  password.addEventListener('change', (c) => {
    password_validation.setAttribute("pattern", c.target.value);
  });
})()