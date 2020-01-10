"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.contrib.auth import views


urlpatterns=[   
    url(r'^$', views.index, name='index'),
    url(r'^uprofile/', views.uprofile, name='uprofile'),
    url(r'^register/', signup, name='signup'),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    url(r'^register/', signup, name='signup'),
    url(r'^accounts/index',views.index,name="index"),
    url(r'^accounts/profile',views.profile,name="profile"),
    url(r'^profile',views.profile,name="profile"),
    
    url(r'^profile/<username>/',views.user_profile, name='user_profile'),
    url(r'^user_profile/<username>/', user_profile, name='user_profile'),
    url(r'^post/<id>', post_comment, name='comment'),
    url(r'^like', like_post, name='like_post'),
    url(r'^search/', search_profile, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
