"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1 import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),

    # path("",views.home,name="home"),
    path("",views.HomeView.as_view(),name="home"),



    # path("addmovie", views.addmovie, name="addmovie"),
    path("addmovie", views.AddMovie.as_view(), name="addmovie"),

    # path("view/<int:p>",views.view,name="view"),
    path("view/<int:pk>", views.Detail.as_view(), name="view"),

    # path("delete/<int:p>",views.delete,name="delete"),
    path("delete/<int:pk>", views.MovieDelete.as_view(), name="delete"),

    # path('edit/<int:p>',views.edit,name="edit")
    path('edit/<int:pk>',views.MovieUpdate.as_view(),name="edit")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
