
    const selectInput = document.querySelector('.select-input');
    const optionsContainer = document.querySelector('.select-options');
    const optionsList = document.querySelectorAll('.select-options div');
    const hiddenInput = document.getElementById('opcion_seleccionada');

    // Mostrar opciones cuando el campo de búsqueda está enfocado
    selectInput.addEventListener('focus', () => {
        optionsContainer.style.display = 'block';
    });

    // Filtrar opciones mientras se escribe en el campo de búsqueda
    selectInput.addEventListener('input', () => {
        const filter = selectInput.value.toLowerCase();
        optionsList.forEach(option => {
            const text = option.textContent.toLowerCase();
            option.style.display = text.includes(filter) ? 'block' : 'none';
        });
    });

    // Seleccionar una opción y establecer su valor en el campo oculto
    optionsList.forEach(option => {
        option.addEventListener('click', () => {
            selectInput.value = option.textContent;
            hiddenInput.value = option.getAttribute('data-value'); // Asigna el valor al campo oculto
            optionsContainer.style.display = 'none';
        });
    });

    // Ocultar opciones cuando se hace clic fuera del menú desplegable
    document.addEventListener('click', (event) => {
        if (!event.target.closest('.select-container')) {
            optionsContainer.style.display = 'none';
        }
    });
