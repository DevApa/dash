from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from documents.views.area.views import *
from documents.views.categoria.views import *
from documents.views.documento.views import *
from documents.views.nivel_acceso.views import *
from documents.views.tipo_documento.views import *

app_name = 'docs'

urlpatterns = [
    url(r'^documento/lista/', login_required(DocumentListView.as_view()), name='list-doc'),
    url(r'^documento/crear/', login_required(DocumentCreateView.as_view()), name='create-doc'),
    url(r'^documento/editar/(?P<pk>\d+)/$', login_required(DocumentUpdateView.as_view()), name='update-doc'),
    url(r'^documento/eliminar/(?P<pk>\d+)/$', login_required(DocumentDeleteView.as_view()), name='delete-doc'),

    url(r'^categoria/lista/', login_required(CategoryListView.as_view()), name='list-category'),
    url(r'^categoria/crear/', login_required(CategoryCreateView.as_view()), name='create-category'),
    url(r'^categoria/editar/(?P<pk>\d+)/$', login_required(CategoryUpdateView.as_view()), name='update-category'),
    url(r'^categoria/eliminar/(?P<pk>\d+)/$', login_required(CategoryDeleteView.as_view()), name='delete-category'),

    url(r'^area/lista/', login_required(AreaListView.as_view()), name='list-area'),
    url(r'^area/crear/', login_required(AreaCreateView.as_view()), name='create-area'),
    url(r'^area/editar/(?P<pk>\d+)/$', login_required(AreaUpdateView.as_view()), name='update-area'),
    url(r'^area/eliminar/(?P<pk>\d+)/$', login_required(AreaDeleteView.as_view()), name='delete-area'),

    url(r'^nivel_acceso/lista/', login_required(LevelAccessListView.as_view()), name='list-level-a'),
    url(r'^nivel_acceso/crear/', login_required(LevelAccessCreateView.as_view()), name='create-level-a'),
    url(r'^nivel_acceso/editar/(?P<pk>\d+)/$', login_required(LevelAccessUpdateView.as_view()), name='update-level-a'),
    url(r'^nivel_acceso/eliminar/(?P<pk>\d+)/$', login_required(LevelAccessDeleteView.as_view()), name='delete-level-a'),

    url(r'^tipo_documento/lista/', login_required(DocumentTypeListView.as_view()), name='list-t-doc'),
    url(r'^tipo_documento/crear/', login_required(DocumentTypeCreateView.as_view()), name='create-t-doc'),
    url(r'^tipo_documento/editar/(?P<pk>\d+)/$', login_required(DocumentTypeUpdateView.as_view()), name='update-t-doc'),
    url(r'^tipo_documento/eliminar/(?P<pk>\d+)/$', login_required(DocumentTypeDeleteView.as_view()), name='delete-t-doc'),
]
