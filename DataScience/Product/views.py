from django.shortcuts import render
from .utility import Product
# Create your views here.
def homepage(request):
    context = dict()
    search = request.GET.get("k")
  
    if search is None:
        pass
    else:
        context["search"] = search
        db = Product(search)
        context['data'] = db.to_dict(orient = "records")
    return render(request,"product/homepage.html", context)