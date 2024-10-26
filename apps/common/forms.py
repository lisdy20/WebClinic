from django import forms

class GenericForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Aplica clases de Bootstrap a todos los campos
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = 'border:1px solid'