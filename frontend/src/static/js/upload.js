//Evento invocado con el submit del formulario
document.getElementById('formularioAnalisis').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const file = this.querySelector('input').files[0];
    const formData = new FormData(event.target);
    
    //Validación de cargue de la imagen
    if (file) {
        //Miestras que llega la respuesta se muestra el loader
        document.querySelector(".loader-container").style.display = "flex";
        //petición a la API
        fetch(API_URL, {
            method: "POST",
            headers: {
                "Accept": "application/json"
            },
            body: formData
            })
        .then(response => {
            //Validación de la respuesta del API
            if (!response.ok) {
                //Si la respuesta no fue satisfactoria lanza la excepción
                return response.json().then(errData => {
                    throw new Error(errData.detail || "Unknown error");
                });
            }
            return response.json()
            })
        .then(data => {
            //Al obtener el json de respuesta se quita el loader y se muestra el resultado
            document.querySelector(".loader-container").style.display = "none";
            const el_respuesta = document.querySelector(".result");
            const formattedJson = JSON.stringify(data, null, 2);
            el_respuesta.querySelector("p").innerHTML = formattedJson;
            el_respuesta.style.display = "block";
            console.log("Success:", formattedJson);
            })
        .catch(error => {
            //Si hay una excepción muestra en el alert que hay error y en la consola el detalle del error.
            document.querySelector(".loader-container").style.display = "none";
            const elemento_alert = document.querySelector(".alert-danger");
            elemento_alert.style.display = "block";
            elemento_alert.querySelector("span").innerHTML = "Ha ocurrido un error, revise la consola para mayor información.";
            console.error("Error:", error);
        });
    } else {
        console.warn('No file selected.');
    }
});

//EventListener para cerrar el alert de error
document.querySelector(".alert-danger button").addEventListener('click', function() {
  document.querySelector(".alert-danger").style.display = "none";
});

//Eventlistener para el cambio de archivo en el formulario
document.querySelector("#formularioAnalisis input").addEventListener("change", function(e) {
  const file = e.target.files[0];
  if (file) {
    const preview = document.getElementById("preview");
    preview.src = URL.createObjectURL(file);
    document.querySelector(".result p").innerHTML = "";
    preview.style.display = "block";
  }
});