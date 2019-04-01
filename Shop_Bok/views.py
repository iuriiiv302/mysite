from .models import Book,Author,Shop
from django.shortcuts import render, get_object_or_404

def shop_all(request):
    return render(request, 'Shop_Bok/ShopBook.html', {})

def bok_detail(request):
    book = Book.objects.all()
    return render(request, "Shop_Bok/bok.html", {"bok": book})

def autor_detail(request):
    autor = Author.objects.all()
    return render(request, 'Shop_Bok/autor.html', {"autor": autor})

def shop_detail(request):
   shop = Shop.objects.all()
   return render(request, 'Shop_Bok/shop.html', {'shop': shop})


def bokinfo(request, pk):
    idBOK = get_object_or_404(Book, pk=pk)
    shops = idBOK.shop_set.all()
    print(shops)
    return render(request, 'Shop_Bok/infoBok.html', {'idBOK': idBOK, "shops": shops})



