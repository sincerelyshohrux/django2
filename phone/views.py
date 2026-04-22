from django.shortcuts import render, redirect
from .models import Phone
# Create your views here.


#list
def phone_list(request):
    phones=Phone.objects.all()
    return render(request, 'list.html', {'phones': phones})

#create
def phone_create(request):
    if request.method == 'POST':
        Phone.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            price=request.POST['price'],
            quantity=request.POST['quantity']
        )
        return redirect('phone_list')
    else:

        return render(request, 'form.html')




    