from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def news(request):
    return render(request, 'news.html')

def our_product(request):
    return render(request, 'our-product.html')

def shop(request):
    return render(request, 'shop.html')

def services(request):
    return render(request, 'services.html')
