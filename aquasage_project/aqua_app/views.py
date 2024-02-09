#  i have created this file - GTA
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Product, Contact
import random


# Create your views here.

def welcome(request):
    return HttpResponse('Teamzeffort    |      welcome Page')
    # return render(request,'tze/business.html')

def dashboard(request):
    return HttpResponse('Teamzeffort    |      dashboard Page')
    # return render(request,'tze/business.html')

def nodeview(request):
    return HttpResponse('Teamzeffort    |      nodeview Page')
    # return render(request,'tze/business.html')

def mapview(request):
    return HttpResponse('Teamzeffort    |      mapview Page')
    # return render(request,'tze/business.html')




# def index(request):
#     # products = Product.objects.all()

#     # all_prods = []
#     # catProds = Product.objects.values('category', 'Product_id')
#     # cats = {item['category'] for item in catProds}
#     # for cat in cats:
#     #     prod = Product.objects.filter(category=cat)
#     #     n = len(products)
#     #     all_prods.append([prod, n]) 

#     params = {
#         'catproducts' : "all_prods",
#         'allproducts' : "products",
#               }

#     return render(request,'aqua_app/index.html', params)



# def about(request):
#     return render(request,'tze/about.html')

# def contact(request):
#     coreMem = Contact.objects.filter(mem_tag="core")
#     teamMem = Contact.objects.filter(mem_tag="team")
#     # print(f"coreMem: {coreMem} \n teamMem: {teamMem}")

#     return render(request, 'tze/contact.html', {'core':coreMem,'team':teamMem })

# def productView(request, myslug):
#     # Fetch the product using the id
#     product = Product.objects.filter(slug=myslug)
#     prodCat = product[0].category
#     # print(prodCat)
#     recproduct = Product.objects.filter(category=prodCat)
#     # print(recproduct)

#     # randomObjects = random.sample(recproduct, 2)
#     randomObjects = random.sample(list(recproduct), 2)


#     return render(request, 'tze/prodView.html', {'product':product[0],'recprod':randomObjects })


# def index(request):
#     return HttpResponse('Teamzeffort    |      index Page')
