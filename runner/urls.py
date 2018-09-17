from django.conf.urls import url
from django.conf.urls import include
from . import views
import superuser
urlpatterns = [                  
        url(r'^generate-form/', views.generate_form, name='test'),
        url(r'authorize-form/', views.authorize_form, name='test2'),
        url(r'^password-new/', views.enter_pass, name='new_pass'),
        url(r'^signup-form/', views.user_signup, name='signup'),
        url(r'^change-password', views.change_password, name='change_password'),
        url(r'^login-naive/', views.login_form, name='login'),
        url(r'^book-taxi/', views.taxi_form, name='book_taxi'),
        url(r'^user-name/', views.get_user_by_name, name='user_name'),
        url(r'^user-detail/(?P<id>\d+)', views.get_user, name='user'),
        url(r'get-user/(?P<id>\d+)', views.get_user_detail, name='user_detail'),
]
