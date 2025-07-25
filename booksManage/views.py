# views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from .models import Books
from .forms import BookForm


class BooksView(View):
    def get(self, request):
        books = Books.objects.all()
        return render(request, 'index.html', {'books': books})

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

        return redirect('index')  # POST成功後に一覧に戻る
    
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
    success_url = reverse_lazy('index')

class BooksUpdateView(generic.UpdateView):
    model = Books
    template_name = "insert.html"
    form_class = BookForm
    
from .forms import SearchForm       # forms.pyからsearchFormクラスをインポート
# 検索機能のビュー
def search(request):
    books = None # 検索結果を格納する変数を初期化
    searchform = SearchForm(request.GET) # GETリクエストで送信したデータが格納される（詳細は解説にて）
        
    # Formに正常なデータがあれば
    if searchform.is_valid():
        query = searchform.cleaned_data['words']
        books_by_title = Books.objects.filter(title__icontains=query)
        books_by_author = Books.objects.filter(author__icontains=query)

        books = books_by_title.union(books_by_author)

    return render(request, 'results.html', {'books':books,'searchform':searchform})