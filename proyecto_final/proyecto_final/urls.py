"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import (index, monstrar_familiares, BuscarFamiliar)
# from blog.views import index as blog_index
from ejemplo.views import (index, buscar, monstrar_familiares,
                            BuscarFamiliar, AltaFamiliar,
                            ActualizarFamiliar, BorrarFamiliar,
                            FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar, FamiliarDetalle)

from tp_final.views import index, PostList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), # ESTA ES LA NUEVA FUNCTION
    path('buscar/', buscar),
    path('mi-familia/', monstrar_familiares), # nueva vista
    # path('blog/', blog_index),
    path('mi-familia/buscar/', BuscarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('success_updated_message/',TemplateView.as_view(template_name="ejemplo/success_updated_message.html")),
    path('tp_final/', index),
    path('tp_final/listar', PostList.as_view())
]
