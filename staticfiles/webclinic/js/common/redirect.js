function go_to_edit(id=null){
    if(id != null){
        const url_edit = document.querySelector('#url_edit').value;
        location.href=`${url_edit}${id}`;
    }
}