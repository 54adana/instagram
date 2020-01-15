from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from Insta import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    
    url('^$', views.index, name='index'),
    url(r'^uprofile/', views.uprofile, name='uprofile'),
    url(r'^accounts/', include ('django.contrib.auth.urls')),

    url(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    url(r'^accounts/registration/', views.signup, name='signup'),
    url(r'^accounts/index',views.index,name="index"),
    url(r'^accounts/profile',views.profile,name="profile"),
    url(r'^profile',views.profile,name="profile"),
    
    url(r'^profile/<username>/',views.user_profile, name='user_profile'),
    url(r'^user_profile/<username>/', views.user_profile, name='user_profile'),
    url(r'^post/<id>', views.post_comment, name='comment'),
    url(r'^like', views.like_post, name='like_post'),
    url(r'^search/', views.search_profile, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)



