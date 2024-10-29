function agregar_medicamento(){
    const url_api_detalles_receta = document.querySelector("#url_api_detalles_receta").value;

    const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const form = document.querySelector("#formdetalle");
    const formData = new FormData(form);

    formData.forEach((value, key) => {
      data[key] = value;
    });
    Swal.fire({
        title: "¿Estás seguro de continuar?",
        text: "¡Una vez continuado no se podrá revertir!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sí, continuar",
        cancelButtonText: "Cancelar"
      }).then( async (result) => {
        if (result.isConfirmed) {
          console.log(data);
          const response = await fetch(url_api_detalles_receta, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFTOKEN':token,
            },
            body: JSON.stringify(data)
          });
          result = await response.json();
          console.log(result.id);
          if (response.ok) {
            Swal.fire({
              title: "¡Agregado!",
              text: result.detail,
              icon: "success"
            }).then((accept) => {
              if (accept.isConfirmed) {
                location.reload();
                console.log("YA")
              }
            });
          } else {
            Swal.fire({
              icon: "error",
              title: "Error...",
              text: `${result.detail}`,
            });
          }
        }
      });
    
    }