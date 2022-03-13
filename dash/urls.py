"""dash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

import dash
from dash import views
from dash import settings
from dash.views import Error404View

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    # Inicio de sesión
    path('jsnCountLogin', views.AjaxEvent.jsnCountLogin, name="jsnCountLogin"),

    path(r'admin/', admin.site.urls),

    # Dashboards View
    path(r'', views.DashboardView.as_view(), name='dashboard'),

    # Accounts
    path('accounts/login/', views.DashboardView.as_view(), name='dashboard'),

    # Layouts
    path(r'layout/', include('layout.urls')),

    # Authencation
    path(r'authentication/', include('authentication.urls')),

    # Configuraciones
    path(r'conf/', include('conf.urls')),

    # Autoevaluacion
    path('inventory/', include('inventory.urls')),

    path('organization/', include('organization.urls')),

    path('documents/', include('documents.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = Error404View.as_view()
handler500 = dash.views.error_500
