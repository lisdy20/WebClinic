function agregar(opcion){
  const url_list = document.querySelector("#url_list").value;
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
      console.log(data);
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFTOKEN':token,
        },
        body: JSON.stringify(data)
      });
      const result = await response.json();
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
                location.href=url_list;
                break;
            }
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
      console.log(id);
      const response = await fetch(`${url}${id}/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFTOKEN':token,
        },
        body: JSON.stringify(data)
      });
      const result = await response.json();
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
          title: "Error",
          text: `${result.detail}`,
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
      title: "¿Estás seguro para dar de baja el registro?",
      text: "Una vez continuado no se podrá revertir.",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "¡Si, dar de baja el registro!",
      cancelButtonText: "Cancelar"
    }).then( async (result) => {
      if (result.isConfirmed) {
      fetch(url, {
        method: 'DELETE',
        headers: {
            'X-CSRFTOKEN':token,
        },
      })
      .then((response)=>{
        if (response.status === 200 || response.status === 204) {
          Swal.fire({
            title: "Dado de baja",
            text: `¡Dado de baja con éxito!`,
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
            text: result.detail,
          });
        }
      })
        
      }
    });
          
  } else {
      console.log("Debe proporcionar un ID de servicio");
  }
}
