# views.py
from datetime import datetime, timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin   # LoginRequiredMixinをインポート
from django.urls import reverse_lazy
from django.views import View, generic
from .models import Books, RentHistory
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
        rent = request.POST.get('rent')
        
        Books.objects.create(
            isbn=isbn,
            title=title,
            author=author,
            publisher=publisher,
            published_date=published_date,
            genre=genre,
            rent=rent,
        )

        return redirect('index')  # POST成功後に一覧に戻る
    
class BooksDetailView(generic.DetailView):
    model = Books
    template_name = 'detail.html'
    context_object_name = 'book'


class BooksInsertView(LoginRequiredMixin, generic.edit.CreateView):
    model = Books
    template_name = 'insert.html'
    form_class = BookForm
    
    
class BooksDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Books
    template_name = "delete.html"
    success_url = reverse_lazy('index')

class BooksUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
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

def lent_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    already_lent = False
    if book.rent:
        already_lent = True
    else:
        book.rent = True
        book.rent_user = request.user
        book.save()
        RentHistory.objects.create(book=book, user=request.user)
    return render(request, 'lent.html', {'book': book, 'already_lent': already_lent})

@login_required
def return_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if book.rent and book.rent_user == request.user:
        book.rent = False
        book.rent_user = None
        book.save()
        # 履歴の返却日時を記録
        history = RentHistory.objects.filter(book=book, user=request.user, returned_at__isnull=True).last()
        if history:
            history.returned_at = datetime.now(timezone.utc)
            history.save()
    return redirect('detail', pk=pk)

@login_required
def my_books(request):
    books = Books.objects.filter(rent_user=request.user, rent=True)
    return render(request, 'my_books.html', {'books': books})

def book_history(request):
    histories = RentHistory.objects.filter(user=request.user).order_by('-lent_at')
    return render(request, 'book_history.html', {'histories': histories})
