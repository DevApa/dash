from django.forms import ModelForm, TextInput, Select, ModelChoiceField, NumberInput
from conf.models import *
from django.db.models import Q
from django.shortcuts import get_object_or_404

ICONOS = Icono.objects.order_by('descripcion')
MODULOS = Modulo.objects.order_by('descripcion')


class ModuloForm(ModelForm):
    class Meta:
        model = Modulo
        fields = '__all__'
        exclude = ['menus']
        labels = {
            'descripcion': 'Descripción:',
            'icon': 'Icono:',
            'orden': 'Orden:',
            'key': 'Key:',
        }
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control', 'placeHolder': 'Ingrese el nombre del modulo'}),
            'orden': TextInput(attrs={'class': 'form-control', 'min': '0', 'type': 'number'}),
            'icon': Select(attrs={'class': 'form-control'}, choices=((x.descripcion, x.descripcion) for x in ICONOS)),
            'key': TextInput(
                attrs={'class': 'form-control', 'placeHolder': 'Generado por el sistema', 'readonly': 'true'}),
        }

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['key'].required = False


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        exclude = ['items']
        labels = {
            'descripcion': 'Descripción:',
            'icon': 'Icono:',
            'orden': 'Orden:',
            'key': 'Key:',
            'modulo_id': 'Módulo:',
            'parent_id': 'Menú:',
            'href': 'Ruta del HTML:',
            'url': 'Url:',
        }
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control', 'placeHolder': 'Ingrese el nombre del modulo'}),
            'orden': TextInput(attrs={'class': 'form-control', 'min': '0', 'type': 'number'}),
            'icon': Select(attrs={'class': 'form-control'}, choices=((x.descripcion, x.descripcion) for x in ICONOS)),
            'href': TextInput(attrs={'class': 'form-control', 'placeHolder': 'Ingrese la url física'}),
            'url': TextInput(attrs={'class': 'form-control', 'placeHolder': 'Ingrese la url lógica'}),
            'key': TextInput(
                attrs={'class': 'form-control', 'placeHolder': 'Generado por el sistema', 'readonly': 'true'}),
        }

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['key'].required = False
        self.fields['href'].required = False
        self.fields['url'].required = False
        self.fields['modulo_id'].required = False
        self.fields['parent_id'].required = False
        self.fields['roles'].required = False
        self.fields['modulo_id'].blank = True
        self.fields['parent_id'].queryset = Menu.objects.none()
        self.fields['modulo_id'].queryset = Modulo.objects.order_by('orden')
        if 'modulo_id' in self.data:
            try:
                if self.data.get('modulo_id'):
                    modulo_id = int(self.data.get('modulo_id'))
                    self.fields['parent_id'].queryset = Menu.objects.filter(modulo_id=modulo_id).order_by(
                        'descripcion').all()
                elif self.data.get('parent_id'):
                    parent_id = int(self.data.get('parent_id'))
                    menu = get_object_or_404(Menu, pk=parent_id)
                    self.fields['parent_id'].queryset = Menu.objects.filter(modulo_id=menu.modulo_id).order_by(
                        'descripcion').all()
                ### Modificar parametros ##
                _mutable = self.data._mutable
                self.data._mutable = True
                if self.data.get('modulo_id') and self.data.get('parent_id'):
                    self.data['modulo_id'] = ""
                self.data['descripcion'] = self.data['descripcion'].capitalize()
                self.data['key'] = self.data['descripcion'].replace(" ", "_").lower() + "_" + self.data['orden']
                self.data._mutable = _mutable
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            if self.instance.modulo_id:
                self.fields['parent_id'].queryset = Menu.objects.filter(
                    Q(modulo_id=self.instance.modulo_id) & Q(href='')).order_by('descripcion')
            elif self.instance.parent_id:
                menu = self.instance.parent_id
                self.fields['parent_id'].queryset = Menu.objects.filter(
                    Q(modulo_id=menu.modulo_id) & Q(href__isnull=True)).order_by('descripcion')


class RolForm(ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'
        labels = {
            'descripcion': 'Descripción:',
        }
        widgets = {
            'descripcion': TextInput(
                attrs={'class': 'form-control', 'placeHolder': 'Ingrese el nombre de la carrera'})
        }
