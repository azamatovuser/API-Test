from django.urls import path
from .views import (
    AccountRegisterView,
    LoginView,
    AccountRetrieveUpdateView,
    AccountListAPIView,
    CommentListCreateAPIView,
)

app_name = 'account'

urlpatterns = [
    path('account/register/', AccountRegisterView.as_view()),
    path('account/login/', LoginView.as_view()),
    path('account/detail/update/<int:pk>/', AccountRetrieveUpdateView.as_view()),
    path('account/list/', AccountListAPIView.as_view()),

    path('comment/list_or_create/', CommentListCreateAPIView.as_view()),
]