from django.contrib import admin
from django.urls import path
from scan import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('nutri_code/',views.nutri_code,name="nutri_code"),
    path('scan/',views.scan,name="scan"),
    path('nutri_code/code/',views.code,name="code"),
]
