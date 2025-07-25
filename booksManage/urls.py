from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.BooksView.as_view(), name="index"),
    path('index/<int:pk>/', views.BooksDetailView.as_view(), name='detail'),
    path('insert/', views.BooksInsertView.as_view(), name='insert'),
    path('<int:pk>/delete/', views.BooksDeleteView.as_view(), name="delete"),
    path('<int:pk>/update/', views.BooksUpdateView.as_view(), name="update"),
    path('search/', views.search, name='search'),

]
