from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Perfil, TipoPerfil
from .forms import PerfilChangeForm, PerfilCreateForm

# Register your models here.
@admin.register(TipoPerfil)
class TipoPerfilAdmin(admin.ModelAdmin):
    list_display=['nombre', 'descripcion']

@admin.register(Perfil)
class PerfilAdmin(UserAdmin):
    form=PerfilChangeForm
    add_form=PerfilCreateForm
    fieldsets=UserAdmin.fieldsets + (
        (
            'Perfil',{
                'fields':(
                    'tipo_perfil',
                    'nombre',
                    'apellido',
                    'colegiado',
                    'direccion',
                    'fechanac',
                    'genero',
                    'telefono',
                )
            }
        ),
    )
    list_display=('username', 'tipo_perfil', 'apellido', 'nombre', 'email', 'is_staff')