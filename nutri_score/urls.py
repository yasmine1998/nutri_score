from django.contrib import admin
from django.urls import path
from scan import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('scan/',views.scan,name="scan"),
    path('nutri_codes/',views.code,name="code"),
]
