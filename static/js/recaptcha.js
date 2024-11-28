<<<<<<< HEAD
// Show Hide Password
document.getElementById("toggle-password-icon").addEventListener("click", function () {
    const passwordField = document.getElementById("password");
    const icon = this;
    if (passwordField.type === "password") {
      passwordField.type = "text";
      icon.classList.remove("fa-lock-open");
      icon.classList.add("fa-lock");
    } else {
      passwordField.type = "password";
      icon.classList.remove("fa-lock");
      icon.classList.add("fa-lock-open");
    }
});

// Google reCAPTCHA
function captchaVerified() {
  document.getElementById("btn").disabled = false;
}

function captchaExpired() {
  document.getElementById("btn").disabled = true;
}
=======
// Show Hide Password
document.getElementById("toggle-password-icon").addEventListener("click", function () {
    const passwordField = document.getElementById("password");
    const icon = this;
    if (passwordField.type === "password") {
      passwordField.type = "text";
      icon.classList.remove("fa-lock-open");
      icon.classList.add("fa-lock");
    } else {
      passwordField.type = "password";
      icon.classList.remove("fa-lock");
      icon.classList.add("fa-lock-open");
    }
});

// Google reCAPTCHA
function captchaVerified() {
  document.getElementById("btn").disabled = false;
}

function captchaExpired() {
  document.getElementById("btn").disabled = true;
}
>>>>>>> e15557ecab5bdcb2311bbce011b5afc1d0f69998
