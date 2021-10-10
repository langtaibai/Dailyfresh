from django.urls import path, re_path
#from .views import register, register_handle
from django.contrib.auth.decorators import login_required
from .views import RegisterView, ActiveView, LoginView, UserInfoView, UserOrderView, AddressView
urlpatterns = [
    # path(r'register', register, name='register'),
    # path(r'register_handle', register_handle, name='register_handle')
    path(r'register', RegisterView.as_view(), name='register'),
    re_path(r'active/(?P<token>.*)', ActiveView.as_view(), name='active'),
    path(r'login', LoginView.as_view(), name='login'),
    path(r'logout', LoginView.as_view(), name='logout'),
    path('', UserInfoView.as_view(),  name='user'),
    path(r'order', UserOrderView.as_view(), name='order'),  # 用户中心-订单页
    path(r'address', AddressView.as_view(), name='address'),  # 用户中心-地址页
]
