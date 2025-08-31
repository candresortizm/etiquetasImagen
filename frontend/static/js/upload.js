document.getElementById('formularioAnalisis').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const file = this.querySelector('input').files[0];

    if (file) {
        document.querySelector(".loader-container").style.display = "flex";
        setTimeout(() => {
        document.querySelector(".loader-container").style.display = "none";
        }, 3000);
        
        console.log("archivo cargado");
    } else {
        console.warn('No file selected.');
    }
});