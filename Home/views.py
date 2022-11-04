from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.models import User, auth,  AnonymousUser
from django.contrib import messages
from .models import Pizza, Orders
# Create your views here.
def home(request):
    if request.user and request.user != AnonymousUser():
        current_user = request.user 
        ordersOfCurrentUser = Orders.objects.filter(User=current_user)
        
        totalOrdersList = []
        for pizzaOrder in ordersOfCurrentUser:
            quantity = pizzaOrder.quantity
            totalOrdersList.append(quantity)
            
        totalOrders = sum(totalOrdersList)
    else:
        totalOrders = 0
    ordersOfCurrentUser = Orders.objects.filter(User=current_user)
    firstobjectofcurrentuser = ordersOfCurrentUser.first()
    #
    context={
    
    'totalOrders':totalOrders,
}
    return render(request, 'Home/index.html', context)

def orders(request):
    try:
        current_username = request.user.username
        user = User.objects.filter(username=current_username).first()
        orders = Orders.objects.filter(User=user)
        price_list = []
        for order in orders:
            price_list.append(order.Pizza_price)
            
        totalPrice = round(sum(price_list), 3)

            
        if request.user and request.user != AnonymousUser():
            current_user = request.user 
            ordersOfCurrentUser = Orders.objects.filter(User=current_user)
            
            totalOrdersList = []
            for pizzaOrder in ordersOfCurrentUser:
                quantity = pizzaOrder.quantity
                totalOrdersList.append(quantity)
                
            totalOrders = sum(totalOrdersList)
        else:
            totalOrders = 0
        ordersOfCurrentUser = Orders.objects.filter(User=current_user)
        firstobjectofcurrentuser = ordersOfCurrentUser.first()
        #
        context={
            'orders':orders,
            'totalOrders':totalOrders,
            'totalPrice':totalPrice,
            'firstobjectofcurrentuser': firstobjectofcurrentuser,
        }
        #
    except Exception:
        pass
    return render(request, "Home/orders.html", context)
    
def increament(request):
    if request.method == "POST":
        if 'order_Id' in request.POST:
            order_Id = request.POST['order_Id']
            pizzaName = request.POST['Pizza_name_']
            order = Orders.objects.filter(id=order_Id)
            order_inst = order.first()
            pizzaPrice = order_inst.Pizza_price
            if order_inst.quantity == 0:
                order.update(quantity = 1)
                return redirect("/orders/")
            else:
                order_inst.quantity +=1
                order.update(quantity = order_inst.quantity)
                pizza_price = Pizza.objects.filter(Pizza_name = pizzaName).first().Pizza_price
                pizzaPrice = round(pizza_price * order_inst.quantity, 3)
                order.update(Pizza_price = pizzaPrice)
                return redirect("/orders/")
                
def decreament(request):
    if request.method == "POST":
        if 'order_Id' in request.POST:
            order_Id = request.POST['order_Id']
            pizzaName = request.POST['Pizza_name_']
            order = Orders.objects.filter(id=order_Id)
            order_inst = order.first()
            pizzaPrice = order_inst.Pizza_price
            
            if order_inst.quantity == 1:
                order.update(quantity = 0)
                order.delete()
                return redirect("/orders/")
            else:
                    order_inst.quantity -= 1
                    order.update(quantity= order_inst.quantity)
                    pizza_price = Pizza.objects.filter(Pizza_name = pizzaName).first().Pizza_price
                    pizzaPrice = round(pizza_price * order_inst.quantity, 3)
                    order.update(Pizza_price = pizzaPrice)
                    return redirect("orders")

            
            
            

def menu(request):
    try:
        if request.user:
            pizzas = Pizza.objects.all()
            current_user = request.user.username
            user = User.objects.filter(username=current_user).first()
            order = Orders.objects.filter(User=user)
            if request.user and request.user != AnonymousUser():
                current_user = request.user 
                ordersOfCurrentUser = Orders.objects.filter(User=current_user)
                
                totalOrdersList = []
                for pizzaOrder in ordersOfCurrentUser:
                    quantity = pizzaOrder.quantity
                    totalOrdersList.append(quantity)
                    
                totalOrders = sum(totalOrdersList)
            else:
                totalOrders = 0
            ordersOfCurrentUser = Orders.objects.filter(User=current_user)
            firstobjectofcurrentuser = ordersOfCurrentUser.first()
            
            try:
                if request.method == "POST":
                    if 'sno' in request.POST:
                        sno = request.POST['sno']
                        #user_logedin = request.POST['user_logedin']
                        pizza_ = Pizza.objects.filter(sno=sno).first()
                        p_name = pizza_.Pizza_name
                        p_desc = pizza_.Pizza_desc
                        p_price = pizza_.Pizza_price
                        
                        allOrders = Orders.objects.filter(User=user, Pizza_name=p_name)
                        if not allOrders:
                            orders = Orders(Pizza_name = p_name, Pizza_desc = p_desc, Pizza_price = p_price, User = user)
                            orders.save()
                            return redirect('menu')
                        else:
                            order_ = Orders.objects.filter(User=user, Pizza_name=p_name)
                            order_quantity = order_.first().quantity
                            if order_quantity == 0:
                                order_.update(quantity=1)
                                return redirect('menu')
                            else:
                                order_quantity +=1
                                order_.update(quantity=order_quantity)
                                return redirect('menu')
                            
                            
            except Exception:
                pass
            
    except Exception:
        pass
    pizzas = Pizza.objects.all()
    context = {
        'pizzas':pizzas,
        'totalOrders': totalOrders,
        'firstobjectofcurrentuser': firstobjectofcurrentuser,
    }
    return render(request, "Home/menu.html", context)
    
    

def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            if 'username' in request.POST:
                f_name = request.POST['f_name']
                l_name = request.POST['l_name']
                email = request.POST['email']
                username = request.POST['username']
                pass1 = request.POST['pass1']
                pass2 = request.POST['pass2']
                if pass1 == pass2:
                    user = User.objects.create_user(username, email, pass1)
                    user.first_name = f_name
                    user.last_name = l_name
                    user.save()
                    user_login = auth.authenticate(username=username, password=pass1)
                    if user_login is not None:
                        auth.login(request, user_login)
                else:
                    messages.warning(request, 'Senhas nao coincidem')
                    return redirect('signup')
    else:
        return redirect('home')
    return render(request, 'Home/signup.html')

def login(request):
    if not request.user.is_authenticated:
        if request.method== "POST":
            if 'user_name' in request.POST:
                user_name = request.POST['user_name']
                user_pass = request.POST['user_pass']
                user = auth.authenticate(username=user_name, password=user_pass)
                if user is not None:
                    auth.login(request, user)
                    messages.success(request, 'Você está Logado')
                    return redirect('home')
    else:
        return redirect('home')
    return render(request, 'Home/login.html')

def deleteOrder(request):
    if request.method == "POST":
        if 'order_Id' in request.POST:
            order_Id = request.POST['order_Id']
            current_user = request.user
            current_order = Orders.objects.get(id=order_Id)
            current_order.delete()
            return redirect('orders')
        

def deleteAll(request):
    if request.method == "POST":
        current_user = request.user
        current_order = Orders.objects.filter(User=current_user)
        current_order.delete()
        return redirect('orders')
    
def orderConfirmed(request):
    if request.method == "POST":
        current_user = request.user
        allOrders = Orders.objects.filter(User=current_user).update(order_confirmed = True)
        return redirect("orders")
    

def profile(request):
    return render(request, "Home/profile.html")