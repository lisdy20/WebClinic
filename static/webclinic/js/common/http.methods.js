function agregar(opcion){
  const url_edit = document.querySelector("#url_edit").value;
  const url = document.querySelector("#url").value;
  const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  console.log(url);
  const form = document.querySelector("#form");
  const formData = new FormData(form);

  var data = {}
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
      const response = await fetch(url, {
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
            console.log(opcion)
            switch (opcion) {
              case 1:
                location.href=`${url_edit}${result.id}/`
                break;
            
              default:
                location.reload();
                break;
            }
          }
        });
      } else {
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: "Something went wrong!",
        });
      }
    }
  });

}

function actualizar(opcion){
  const id = document.querySelector("#id").value;
  const url = document.querySelector("#url").value;
  const url_list = document.querySelector("#url_list").value;
  const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  console.log(url);
  const form = document.querySelector("#form");
  const formData = new FormData(form);

  var data = {}
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
      const response = await fetch(`${url}${id}/`, {
        method: 'PUT',
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
            console.log(opcion)
            switch (opcion) {
              case 1:
                break;
              default:
                location.href=url_list
                break;
            }
          }
        });
      } else {
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: "¡Ha ocurrido un error!",
        });
      }
    }
  });

}

function eliminar(id=null){

  const url = `${document.querySelector("#url").value}${id}/`;
  const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  console.log(url);
  if(id!= null){
    Swal.fire({
      title: "Are you sure?",
      text: "You won't be able to revert this!",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Yes, delete it!"
    }).then((result) => {
      if (result.isConfirmed) {
      fetch(url, {
        method: 'DELETE',
        headers: {
            'X-CSRFTOKEN':token,
        },
      })
        .then(response => {
          if (response.ok) {
            Swal.fire({
              title: "Deleted!",
              text: "Your file has been deleted.",
              icon: "success"
            }).then((accept) => {
              if (accept.isConfirmed) {
                location.reload();
              }
            });
          } else {
            Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "Something went wrong!",
            });
          }
        }).catch(error => {
        console.error('Hubo un problema con la solicitud:', error);
      });
        
      }
    });
          
  } else {
      console.log("Debe proporcionar un ID de servicio");
  }
}
