from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BooksView.as_view(), name="books_list"),
    path('books/<int:pk>/', views.BooksDetailView.as_view(), name='detail'),
    path('insert/', views.BooksInsertView.as_view(), name='insert'),
    path('<int:pk>/delete/', views.BooksDeleteView.as_view(), name="delete"),
    path('<int:pk>/update/', views.BooksUpdateView.as_view(), name="update"),

]
