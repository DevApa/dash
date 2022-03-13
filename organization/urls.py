from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from organization.views.departamento.views import *
from organization.views.facultad.views import *
from organization.views.unidad_academica.views import *
from organization.views.universidad.views import *

app_name = 'org'

urlpatterns = [
    url(r'^universidad/lista/', login_required(UniversityListView.as_view()), name='uni-list'),
    url(r'^universidad/crear/', login_required(UniversityCreateView.as_view()), name='uni-create'),
    url(r'^universidad/editar/(?P<pk>\d+)/$', login_required(UniversityUpdateView.as_view()), name='uni-update'),
    url(r'^universidad/eliminar/(?P<pk>\d+)/$', login_required(UniversityDeleteView.as_view()), name='uni-delete'),

    url(r'^facultad/editar/', login_required(SchoolOfListView.as_view()), name='fac-list'),
    url(r'^facultad/crear/', login_required(SchoolOfCreateView.as_view()), name='fac-create'),
    url(r'^facultad/editar/(?P<pk>\d+)/$', login_required(SchoolOfUpdateView.as_view()), name='fac-update'),
    url(r'^facultad/eliminar/(?P<pk>\d+)/$', login_required(SchoolOfDeleteView.as_view()), name='fac-delete'),

    url(r'^unidad_academica/lista/', login_required(AcademicUnitListView.as_view()), name='uac-list'),
    url(r'^unidad_academica/crear/', login_required(AcademicUnitCreateView.as_view()), name='uac-create'),
    url(r'^unidad_academica/editar/(?P<pk>\d+)/$', login_required(AcademicUnitUpdateView.as_view()), name='uac-update'),
    url(r'^unidad_academica/eliminar/(?P<pk>\d+)/$', login_required(AcademicUnitDeleteView.as_view()), name='uac-delete'),

    url(r'^departamento/lista/', login_required(DepartmentListView.as_view()), name='dep-list'),
    url(r'^departamento/crear/', login_required(DepartmentCreateView.as_view()), name='dep-create'),
    url(r'^departamento/editar/(?P<pk>\d+)/$', login_required(UniversityUpdateView.as_view()), name='dep-update'),
    url(r'^departamento/eliminar/(?P<pk>\d+)/$', login_required(DepartmentDeleteView.as_view()), name='dep-delete'),
]
