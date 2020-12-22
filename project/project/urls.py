from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from fb_auth import views as fb_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', fb_views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', fb_views.home, name='home'),
    path('create_place', fb_views.create_place, name='create-place'),
    path('place_detail/<int:place_id>/', fb_views.place_detail, name='place-detail'),
]
