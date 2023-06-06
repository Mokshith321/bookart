from django.shortcuts import render
from .models import book
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, reverse
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
import razorpay

# from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html')

def booking(request):
    books  = book.objects.all()
    return render(request, 'booking.html',{'books':books})

# @login_required
def renting(request):
    if(request.method == "POST"):
        # get the book details and store in the database
        title = request.POST['name']
        cost = int(request.POST['cost'])
        cost = cost * 100
        if(len(request.FILES)!=0):
            image = request.FILES['image']
        book1 = book()
        book1.title = title
        book1.cost = cost
        book1.img = image
        book1.user = request.user
        book1.save()
        books = book.objects.filter(user=request.user)
        return render(request, 'renting.html',{'books':books})
    else:
        if request.user.is_authenticated:
            books = book.objects.filter(user=request.user)
            if(books.exists()):
                return render(request, 'renting.html',{'books':books})
            else:
                return render(request, 'renting.html',{'message':"Rents your books here."})
        else:
            return redirect(reverse('login'))

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request,'profile.html')

def book_details(request,book_id):
    if request.user.is_authenticated:
        book_obj = get_object_or_404(book, id=book_id)
        today = datetime.now().date()
        date_after_seven_days = today + timedelta(days=7)
        context = {
            'cost':book_obj.cost / 100,
            'book': book_obj,
            'today': today,
            'date_after_seven_days': date_after_seven_days
        }
        client = razorpay.Client(auth=("rzp_test_qyDzuiKyrhzxy2", "AmaJxnLdHO87uVdbJWO0JbyA"))
        data = { "amount": book_obj.cost, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        return render(request,'book-details.html',{'payment':payment, **context})
    else:
        return redirect(reverse('login'))
