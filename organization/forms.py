from django.forms import *

from organization.models import University, Department, AcademicUnit, SchoolOf


class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = ['name', 'address', 'phone', 'rector', 'type', 'foundation_date']
        labels = {
            'name': 'Nombre:',
            'address': 'Dirección:',
            'phone': 'Teléfono:',
            'rector': 'Rector',
            'type': 'Tipo',
            'foundation_date': 'Fecha fundación'
        }
        widgets = {
            'name':
                TextInput(attrs={'class': 'form-control', 'placeHolder': 'Ingrese el nombre de la universidad'}),
            'address':
                TextInput(attrs={'class': 'form-control', 'placeHolder': 'Ingrese el dirección de la universidad'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeHolder': 'Ingrese el teléfono de la universidad',
                                      'onkeypress': 'return validaNumericos(event)'}),
            'rector': TextInput(attrs={'class': 'form-control', 'placeHolder': 'Rector de la institución'}),
            'type': Select(attrs={'class': 'form-control'}),
            'foundation_date': DateInput(attrs={'class': 'form-control', 'type': 'date'},
                                         format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['foundation_date'].input_formats = ('%Y-%m-%d',)
        self.fields['address'].required = False
        self.fields['phone'].required = False


class SchoolOfForm(ModelForm):
    class Meta:
        model = SchoolOf
        fields = ['university', 'name', 'address', 'phone', 'dean', 'foundation_date', 'date_input']
        labels = {
            'university': 'Universidad',
            'name': 'Nombre:',
            'address': 'Dirección:',
            'phone': 'Teléfono:',
            'dean': 'Decano',
            'foundation_date': 'Fecha fundación',
            'date_input': 'Hora Ingreso',
        }
        widgets = {
            'university': Select(attrs={'class': 'form-control'}),
            'name':
                TextInput(attrs={'class': 'form-control', 'placeHolder': 'Ingrese el nombre de la facultad'}),
            'address':
                TextInput(attrs={'class': 'form-control', 'placeHolder': 'Ingrese el dirección de la facultad'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeHolder': 'Ingrese el teléfono de la facultad',
                                      'onkeypress': 'return validaNumericos(event)'}),
            'dean': TextInput(attrs={'class': 'form-control', 'placeHolder': 'Decano de la institución'}),
            'foundation_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}
                                         , format='%Y-%m-%d'),
            'date_input': TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['university'].empty_label = 'Seleccione una institución '
        self.fields['university'].widget.attrs['autofocus'] = True
        self.fields['foundation_date'].input_formats = ['%Y-%m-%d']
        self.fields['address'].required = False
        self.fields['phone'].required = False


class AcademicUnitForm(ModelForm):
    class Meta:
        model = AcademicUnit
        fields = ['schoolOf', 'name', 'address', 'phone', 'director', 'foundation_date']
        labels = {
            'schoolOf': 'Facultad',
            'name': 'Nombre:',
            'address': 'Dirección:',
            'phone': 'Teléfono:',
            'director': 'Director',
            'foundation_date': 'Fecha fundación'
        }
        widgets = {
            'schoolOf': Select(attrs={'class': 'form-control'}),
            'name':
                TextInput(attrs={'class': 'form-control', 'placeHolder': 'Ingrese el nombre de la Unidad Académica'}),
            'address':
                TextInput(
                    attrs={'class': 'form-control', 'placeHolder': 'Ingrese el dirección de la Unidad Académica'}),

            'phone': TextInput(attrs={'class': 'form-control',
                                      'placeHolder': 'Ingrese el teléfono de la Unidad Académica',
                                      'onkeypress': 'return validaNumericos(event)'}),
            'director': TextInput(attrs={'class': 'form-control', 'placeHolder': 'Director de la institución'}),
            'foundation_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}
                                         , format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['schoolOf'].empty_label = 'Seleccione una Facultad'
        self.fields['schoolOf'].widget.attrs['autofocus'] = True
        self.fields['foundation_date'].input_formats = ['%Y-%m-%d']
        self.fields['address'].required = False
        self.fields['phone'].required = False
        self.fields['director'].required = False


class DepartmentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foundation_date'].input_formats = ['%Y-%m-%d']
        self.fields['academic_unit'].empty_label = 'Seleccione una Departamento'
        self.fields['academic_unit'].widget.attrs['autofocus'] = True

    class Meta:
        model = Department
        fields = ['name', 'phone', 'boss', 'foundation_date', 'academic_unit']

        labels = {
            'academic_unit': 'Unidad Académica',
            'name': 'Nombre',
            'phone': 'Teléfono',
            'boss': 'Jefe',
            'foundation_date': 'Fecha Fundación'
        }

        widgets = {
            'academic_unit': Select(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Departamento'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono '}),
            'boss': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese jefe de área'}),
            'foundation_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}
                                         , format='%Y-%m-%d')
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

