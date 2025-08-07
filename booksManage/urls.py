from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.BooksView.as_view(), name="index"),
    path('index/<int:pk>/', views.BooksDetailView.as_view(), name='detail'),
    path('insert/', views.BooksInsertView.as_view(), name='insert'),
    path('<int:pk>/delete/', views.BooksDeleteView.as_view(), name="delete"),
    path('<int:pk>/update/', views.BooksUpdateView.as_view(), name="update"),
    path('search/', views.search, name='search'),
    path('lent/<int:pk>/', views.lent_book, name='lent'),
    path('return/<int:pk>/', views.return_book, name='return_book'),
    path('mybooks/', views.my_books, name='my_books'),
    path('history/', views.book_history, name='book_history'),
    path('detail/<int:pk>/review/', views.review_create, name='review_create'),

]
