
from django.urls import path
from .views import RegisterView,UserLoginView,UserLogoutView,Activate,MoreInfoDetailUpdateView,UserDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register' ),
    path('login/', UserLoginView.as_view(), name='login' ),
    path('logout/', UserLogoutView.as_view(), name='logout' ),
    path('active/',Activate.as_view() ),
    path('user/<str:username>/', MoreInfoDetailUpdateView.as_view(), name='moreinfo-detail-update'),
    path('user/delete/<str:username>/', UserDeleteView.as_view(), name='user-delete'),
]
