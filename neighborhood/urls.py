from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('register/',views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registrations/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registrations/logout.html'), name='logout'),
    path('search/', views.search_businesses, name='search_results'),
    path('business/(\d+)', views.get_business, name='business_results'),
    path('new/business', views.new_business, name='new-business'),
    path('new/post', views.new_post, name='new-post'),
    path('profile/', views.user_profiles, name='profile'),
    path('tinymce/', include('tinymce.urls')),
     
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)