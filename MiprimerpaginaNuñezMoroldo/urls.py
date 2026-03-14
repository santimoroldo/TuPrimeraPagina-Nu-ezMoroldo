from django.contrib import admin
from django.urls import path, include # Agregamos 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), # Esto le dice al proyecto que use las URLs de tu app
]