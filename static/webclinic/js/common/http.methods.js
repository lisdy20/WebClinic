function agregar(){
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
    title: "Are you sure?",
    text: "You won't be able to revert this!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Yes, delete it!"
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
    }
  });

}

async function agregar_seguir_editando(){
  const url_edit = document.querySelector("#url_edit");
  const url = document.querySelector("#url").value;
  const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  const form = document.querySelector("#form");
  const formData = new FormData(form);

  var data = {}
  formData.forEach((value, key) => {
    data[key] = value;
  });

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
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFTOKEN':token,
      },
      body: JSON.stringify(data)
    })
      .then(response => {
        if (response.ok) {
          console.log(response.json())
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


