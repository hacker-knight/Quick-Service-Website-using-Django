from django.shortcuts import render,redirect
from .models import*
from django.forms import inlineformset_factory
from .forms import*
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.
def admin_signup(request):
    form=A_signup()
    if request.method == 'POST':
        print('Inside if request .method is Post')
        form=A_signup(request.POST)
        if form.is_valid():
            print('Inside form is valid')
            form.save()
            context={'astat': True}
            return render(request,'admin_signup.html',context)
        else:
            context={'astat': False}
            return render(request,'admin_signup.html',context)
    return render(request,'admin_signup.html')
def admin_signin(request):
    return render(request,'admin_signin.html')

def admin_ui(request):
    shops=Shop.objects.all()
    users=Client.objects.all()
    orders=Orders.objects.all()
    context={
        'shops' : shops,
        'users': users,
        'orders': orders,
    }
    if request.method == 'POST':
        form=A_Signin(request.POST)
        if form.is_valid():
            s_un=request.POST['a_uname']
            s_ps=request.POST['a_psw']
            context={
                'shops' : shops,
                'users': users,
                'orders': orders,
                'astat': True,
                's_un': s_un,
                's_ps' : s_ps,
                'Ordered':'Ordered'
            }
            for shop in shops:
                if shop.uname == request.POST['a_uname'] and shop.psw==request.POST['a_psw'] :
                    return render(request,'admin_ui.html',context)
                else:  
                    context={
                        'astat': False
                    }
            return render(request,'admin_signin.html',context)  
        else:
            return render(request,'admin_signin.html')
    else:
        return render(request,'admin_ui.html')

def admin_prod(request,s_un):
    products=Product.objects.all()
    context={
        'products':products,
        's_un':s_un
    }
    return render(request,'admin_prod.html',context)

def a_product(request,s_un):
    form=A_Prod()
    if request.method == 'POST':
        form=A_Prod(request.POST, request.FILES)
        if form.is_valid():
            if s_un == request.POST['shop_un']:
                form.save()
                context={
                    'prod_stat': True,
                    's_un':s_un
                }
                return render(request,'admin_prod_add.html',context)
            else:
                context={
                    'prod_stat':False,
                    's_un':s_un
                }
                return render(request,'admin_prod_add.html',context)
    else:
        return render(request,'admin_prod_add.html',context={'s_un':s_un})

def edit_prod(request,s_un,ok):
    product=Product.objects.get(id=ok)
    form=A_Prod(instance=product)
    context={
        's_un':s_un,
        'ok':ok,
        'product':product
    }
    if request.method == 'POST':
        form=A_Prod(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return admin_prod(request,s_un)
    return render(request,'admin_edit_prod.html',context)

def admin_del_p(request,s_un,ok):
    del_prod=Product.objects.get(id=ok)
    del_prod.delete()
    
    products=Product.objects.all()
    context={
        'products':products,
        's_un':s_un
    }
    return render(request,'admin_prod.html',context)

def login(request):
    form=Signup()
    if request.method == 'POST':
        form=Signup(request.POST)
        if form.is_valid():
            form.save()
            context={
                'stat': True
            }
            return render(request,'test.html',context)
        else:
            context={'stat': False}
            return render(request,'test.html',context)
        return redirect('/')
    return render(request,'test.html')

def signin(request):
    return render(request,'signin.html')
    
def home(request):
    shops=Shop.objects.all()
    users=Client.objects.all()
    context={
            'shops': shops,
            'users': users
        }
    if request.method == 'POST':
        form=Signin(request.POST)
        if form.is_valid():
            for user in users:
                if user.email == request.POST['uname'] and user.psw == request.POST['psw']:
                    ck=user.id
                    user=Client.objects.get(id=ck)
                    context={
                        'shops':shops,
                        'user':user,
                        'ck':user.id,
                        'stat': True
                    }
                    return render(request,'homepage.html',context)
                    break
            else:
                context={
                'stat': False
                }
                return render(request,'signin.html',context)
        else :
            return HttpResponse('Form invalid')

def home1(request,ck):
    shops=Shop.objects.all()
    user=Client.objects.get(id=ck)
    context={
        'shops': shops,
        'user': user,
        'ck' : ck,
    }
    return render(request,'homepage.html',context)
    
def shop(request,s_id,ck):
    li=s_id
    shops=Shop.objects.all()
    products=Product.objects.all()
    categories=Categories.objects.all()
    context={'products': products,'shops': shops, 'categories': categories, 's_un': li, 'ck':ck}
    return render(request,'shop.html',context)

def add_to_cart(request,ck):
    if request.method == 'POST':
        form=Add_Order(request.POST)
        if form.is_valid():
            form.save()
    products=Product.objects.all()
    item=Orders.objects.filter(client=ck,p_deliver='Cart')
    tot=list(Orders.objects.filter(client=ck,p_deliver='Cart').aggregate(Sum('p_cost')).values())[0]
    print("Total is",tot)
    context_cart={
        'products':products,
        'item': item,
        'ck':ck,
        'sum':tot,
    }
    return render(request,'addcart.html',context_cart)

def prod(request,s_id,prod_cat,name,cost,ck):
    products=Product.objects.all()
    context={'products':products,'shop':s_id,'cat':prod_cat,'prod':name,'prod_cost':cost, 'ck':ck}
    return render(request,'product.html',context)

def about(request,ck):
    return render(request,'about.html',context={'ck':ck})

def del_p(request,p,ck):
    del_prod=Orders.objects.get(id=p)
    del_prod.delete()
    
    products=Product.objects.all()
    item=Orders.objects.filter(client=ck,p_deliver='Cart')
    tot=list(Orders.objects.filter(client=ck,p_deliver='Cart').aggregate(Sum('p_cost')).values())[0]
    print("Total is",tot)
    context_cart={
        'products':products,
        'item': item,
        'ck':ck,
        'sum':tot,
    }
    return render(request,'addcart.html',context_cart)

def conf_ord(request,ck):
    client=Client.objects.get(id=ck)
    ords=Orders.objects.filter(client=ck)
    AddOrderSet= inlineformset_factory(Client,Orders, fields=('p_name','p_deliver','p_cost'),extra=0,can_order=True)
    formset = AddOrderSet(instance=client)
    if request.method == 'POST':
        formset = AddOrderSet(request.POST, instance=client)
        if formset.is_valid():
            formset.save()
            return render(request,'confirmation.html',context={'ck':ck})
    context={
        'ck':ck,
        'formset':formset
    }
    return render(request,'placeorder.html',context)

def track(request,ck):
    orders=Orders.objects.filter(client=ck)
    products=Product.objects.all()
    context={'orders': orders, 'products': products, 'Ordered':'Ordered', 'ck':ck}
    return render(request,'trackorder.html',context)

def sub_p(request,ck,pk):
    order=Orders.objects.get(id=pk)
    form=Final_Order(instance=order)
    if request.method == 'POST':
        form=Final_Order(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return history(request,ck)

def history(request,ck):
    orders=Orders.objects.filter(client=ck)
    products=Product.objects.all()
    context={'orders': orders,'products':products, 'ck':ck, 'Received':'Received'}
    return render(request,'history.html',context)
