from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    num_book_title_icontain_how = Book.objects.filter(title__icontains = 'how').count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        #index()最後將會導向到下列這個.html檔案:index.html
        'index.html',
        #並且把剛剛從db取得的物件傳送到index.html
        # context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,'num_book_title_icontain_how':num_book_title_icontain_how},
    )