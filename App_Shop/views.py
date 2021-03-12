from django.shortcuts import render

#import views
from django.views.generic import ListView, DetailView

#models
from App_Shop.models import Product, Category

#mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        print(context)
        context['categories'] = Category.objects.all()
        print(context['categories'])
        #dic = {'categories': categories}
        #return render(request, self.template_name,context=dic)
        if self.request.method == 'GET':
            search = self.request.GET.get('search','')
            # results = Product.objects.filter(name__icontains=search)
            results = Product.objects.filter(name__icontains=search)
            context['results'] = results
            print(results)
            context['search'] = search
        return context




class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    tamplate_name = 'App_Shop/product_detail.html'
    





def customCategory(request, pk):
    categories = Category.objects.all()
    category = Category.objects.filter(pk=pk)[0]
    products = Product.objects.filter(category=category)
    customize = True
    print(products)
    dic = {'products':products, 'customize':customize, 'categories':categories}
    return render(request,'App_Shop/home.html',context=dic)
