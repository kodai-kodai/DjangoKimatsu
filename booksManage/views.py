# views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from .models import Books
from .forms import BookForm


class BooksView(View):
    def get(self, request):
        books = Books.objects.all()
        return render(request, 'books_list.html', {'books': books})

    def post(self, request):
        isbn = request.POST.get('isbn')
        title = request.POST.get('title')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        published_date = request.POST.get('published_date')
        genre = request.POST.get('genre')

        Books.objects.create(
            isbn=isbn,
            title=title,
            author=author,
            publisher=publisher,
            published_date=published_date,
            genre=genre
        )

        return redirect('books_list')  # POST成功後に一覧に戻る
    
class BooksDetailView(generic.DetailView):
    model = Books
    template_name = 'detail.html'
    context_object_name = 'book'


class BooksInsertView(generic.CreateView):
    model = Books
    template_name = 'insert.html'
    form_class = BookForm
    
    
class BooksDeleteView(generic.DeleteView):
    model = Books
    template_name = "delete.html"
    success_url = reverse_lazy('books_list')

class BooksUpdateView(generic.UpdateView):
    model = Books
    template_name = "insert.html"
    form_class = BookForm