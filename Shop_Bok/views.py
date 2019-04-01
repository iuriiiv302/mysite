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
    return render(request, 'Shop_Bok/infoBok.html', {'idBOK': idBOK, 'shops': shops})


def Autorinfo (request,pk):
    idAutor = get_object_or_404(Author,pk=pk)
    autobok = Book.objects.filter(author_id=idAutor)
    print(autobok)
    return render(request,'Shop_Bok/infoAutor.html',{'idAutor':idAutor,'autobok':autobok})

def shopinfo (request,pk):
    idShop = get_object_or_404(Shop,pk=pk)
    Book = idShop. books.all()
    print(Book)
    return render(request,'Shop_Bok/infoShop.html',{'idShop':idShop,'shops':Book})


