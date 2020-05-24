const signUpButton = document.getElementById('signUp');
const backButton = document.getElementById('back');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

backButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});