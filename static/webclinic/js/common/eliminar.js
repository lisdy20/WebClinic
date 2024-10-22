function eliminar(id=null){
    const url = `${document.querySelector("#url").value}${id}/`;
    const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    console.log(url);
    if(id!= null){
        fetch(url, {
            method: 'DELETE',
            headers: {
                'X-CSRFTOKEN':token,
            },
          })
            .then(response => {
              if (response.ok) {
                console.log(`Servicio con ID ${id} eliminado correctamente.`);
                location.reload();
              } else {
                throw new Error('No se pudo eliminar el servicio');
              }
            })
            .catch(error => {
              console.error('Hubo un problema con la solicitud:', error);
            });
    } else {
        console.log("Debe proporcionar un ID de servicio");
    }
}