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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import (index, monstrar_familiares, BuscarFamiliar)
# from blog.views import index as blog_index
from ejemplo.views import (index, buscar, monstrar_familiares,
                            BuscarFamiliar, AltaFamiliar,
                            ActualizarFamiliar, BorrarFamiliar,
                            FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar, FamiliarDetalle)

from tp_final.views import (index, PostList, PostCrear, PostActualizar, PostDetalle, PostBorrar, 
                            PostActualizar, UserSignUp, UserLogin, UserLogout, AvatarActualizar, 
                            UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle,
                            MensajeBorrar)

from django.contrib.admin.views.decorators import staff_member_required
                

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
    path('tp_final/', index, name = "tp_final-index"),
    path('tp_final/listar/', PostList.as_view(), name = "tp_final-listar"),
    path('tp_final/crear/', staff_member_required(PostCrear.as_view()), name = "tp_final-crear"),
    path('tp_final/<int:pk>/detalle/', PostDetalle.as_view(), name = "tp_final-detalle"),
    path('tp_final/<int:pk>/borrar/', PostBorrar.as_view(), name = "tp_final-borrar"),
    path('tp_final/<int:pk>/actualizar/', PostActualizar.as_view(), name = "tp_final-actualizar"),
    path('tp_final/signup/', UserSignUp.as_view(), name = 'tp_final-signup'),
    path('tp_final/login/', UserLogin.as_view(), name = 'tp_final-login'),
    path('tp_final/logout/', UserLogout.as_view(), name = 'tp_final-logout'),
    path('tp_final/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="tp_final-avatars-actualizar"),
    path('tp_final/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="tp_final-users-actualizar"),
    path('tp_final/mensajes/crear/', MensajeCrear.as_view(), name="tp_final-mensajes-crear"),
    path('tp_final/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="tp_final-mensajes-detalle"),
    path('tp_final/mensajes/listar/', MensajeListar.as_view(), name="tp_final-mensajes-listar"),
    path('tp_final/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="tp_final-mensajes-borrar"),
    path('tp_final/mensajes/borrar/', MensajeListar.as_view(), name="tp_final-mensajes-listar"),
    path('tp_final/about', TemplateView.as_view(template_name='tp_final/about.html'), name="tp_final-about"),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)