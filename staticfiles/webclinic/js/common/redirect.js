function go_to_edit(id=null){
    if(id != null){
        const url_edit = document.querySelector('#url_edit').value;
        location.href=`${url_edit}${id}`;
    }
}

function regresar(){
    const url_list = document.querySelector('#url_list').value;

    location.href=url_list;
}

function regresar_cita(){
    // Crea un objeto URLSearchParams usando la cadena de consulta de la URL actual
    const urlParams = new URLSearchParams(window.location.search);

    // Recupera los valores de los parámetros
    const cita = urlParams.get('cita');
    const url_cita = document.querySelector('#url_cita').value;
    location.href=url_cita+cita+"/";
}

function lista_antecedentes(paciente,cita){
    if(paciente != null){
        const url_antecedentes = document.querySelector('#url_antecedentes').value;
        location.href=`${url_antecedentes}${paciente}/?cita=${cita}`;
    }
}