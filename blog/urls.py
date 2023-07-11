from django.urls import path

from . import views


urlpatterns = [
    path(route='', view=views.BlogListView.as_view(), name='blog_list'),
    path('signup/', views.SignupPageView.as_view(), name='signup'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('create/', views.BlogCreateView.as_view(), name='blog_create'),
    path(route='<int:pk>/', view=views.BlogDetailView.as_view(), name='blog_detail'),
    path(route='<int:pk>/update', view=views.BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),

    path('api/blogposts/', views.BlogAPIView.as_view(), name='blogpost-list'),
    path('api/blogposts/<int:pk>/', views.BlogAPIView.as_view(), name='blogpost-detail'),
]