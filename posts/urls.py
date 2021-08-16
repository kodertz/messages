from django.urls import path
from .views import HomePage, PostDeleteView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'delete'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name = 'edit'),
    path('post/new/', PostCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'detail'),
    path('', HomePage.as_view(), name = 'home'),
]