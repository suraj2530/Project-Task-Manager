
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.api.urls')),
    # path('api-auth/', include('rest_framework.urls'))

    path('accounts/', include('user_app.api.urls')) 


]
