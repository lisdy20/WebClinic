from django import forms

class GenericForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
             # Configura el widget para los campos DateTimeField
            if isinstance(field, forms.DateTimeField):
                # Configura el widget para que use el formato YYYY-MM-DD
                field.widget = forms.DateInput(
                    attrs={
                        'type': 'date',  # Tipo de input para selección de fecha
                        'class': 'form-control',
                        'style': 'border:1px solid',
                    }
                )
                # Establece el valor inicial en el formato adecuado si existe
                if field.initial:
                    field.initial = field.initial.strftime('%Y-%m-%d')
            # Si el campo no es checkbox o radio, aplica 'class' y 'style'
            if not isinstance(field.widget, forms.CheckboxInput) and not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['style'] = 'border:1px solid'