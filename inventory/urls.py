from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from inventory.views.marca.views import *
from inventory.views.tipo_equipo.views import *

app_name = 'inventory'

urlpatterns = [
    url(r'^marca/lista/', login_required(BrandListView.as_view()), name='list-brand'),
    url(r'^marca/crear/', login_required(BrandCreateView.as_view()), name='create-brand'),
    url(r'^marca/editar/(?P<pk>\d+)/$', login_required(BrandUpdateView.as_view()), name='update-brand'),
    url(r'^marca/eliminar/(?P<pk>\d+)/$', login_required(BrandDeleteView.as_view()), name='delete-brand'),

    url(r'^tipo_equipo/lista/', login_required(EquipmentTypeListView.as_view()), name='list-eq-type'),
    url(r'^tipo_equipo/crear/', login_required(EquipmentTypeCreateView.as_view()), name='create-eq-type'),
    url(r'^tipo_equipo/editar/(?P<pk>\d+)/$', login_required(EquipmentTypeUpdateView.as_view()), name='update-eq-type'),
    url(r'^tipo_equipo/eliminar/(?P<pk>\d+)/$', login_required(EquipmentTypeDeleteView.as_view()), name='delete-eq-type'),

]

