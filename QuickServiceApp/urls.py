from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin_signup',views.admin_signup,name='admin_signup'),
    path('admin_signin',views.admin_signin,name='admin_signin'),
    path('admin_ui',views.admin_ui,name='admin_ui'),
    path('a_product/<str:s_un>',views.a_product,name='a_product'),
    path('admin_prod/<str:s_un>',views.admin_prod,name='admin_prod'),
    path('edit_prod/<str:s_un>/<str:ok>',views.edit_prod,name='edit_prod'),
    path('admin_del_p/<str:s_un>/<str:ok>',views.admin_del_p,name='admin_del_p'),
    path('',views.signin),
    path('signup',views.login,name='login'),
    path('home',views.home,name='home'),
    path('home/<str:ck>',views.home1),
    path('shop/<str:s_id>/<str:ck>',views.shop),
    path('track/<str:ck>',views.track),
    path('sub_p/<str:ck>/<str:pk>',views.sub_p,name='sub_p'),
    path('cart/<str:ck>',views.add_to_cart,name='add_to_cart'),
    path('history/<str:ck>',views.history),
    path('prod/<str:s_id>/<str:prod_cat>/<str:name>/<int:cost>/<str:ck>',views.prod,name='prod'),
    path('about/<str:ck>',views.about,name='about'),
    path('del_p/<str:p>/<str:ck>',views.del_p,name='del_p'),
    path('conf_ord/<str:ck>',views.conf_ord,name='conf_ord'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)