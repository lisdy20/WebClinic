from django import forms

class GenericForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Si el campo no es checkbox o radio, aplica 'class' y 'style'
            if not isinstance(field.widget, forms.CheckboxInput) and not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['style'] = 'border:1px solid'