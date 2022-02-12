from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "productApp/index.html")


def electronics(request):
    product_dict = {
        "heading": "Electronics Products",
        "product1": "Laptops",
        "product2": "Mobiles",
        "product3": "Cameras"
    }
    return render(request, "productApp/products.html", product_dict)


def toys(request):
    product_dict = {
        "heading": "Toys Products",
        "product1": "Teddy Bear",
        "product2": "Remote Car",
        "product3": "Pistol Gun"
    }
    return render(request, "productApp/products.html", product_dict)


def shoes(request):
    product_dict = {
        "heading": "Shoes Products",
        "product1": "Sparx",
        "product2": "Woodland",
        "product3": "Adidas"
    }
    return render(request, "productApp/products.html", product_dict)
