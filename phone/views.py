from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone
# Create your views here.



# LIST 
def phone_list(request):
    phons = Phone.objects.all()
    context = {
        'phons': phons
    }
    return render(request, 'list.html', context)


# CREATE 
def phone_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        Phone.objects.create(
            title=title,
            description=description,
            price=price,
            quantity=quantity,
        )
        return redirect('phone_list')

    return render(request, 'create.html')


# UPDATE 
def phone_update(request, pk):
    phon = get_object_or_404(Phone, pk=pk)
    if request.method == "POST":
        phon.title = request.POST.get('title')         
        phon.description = request.POST.get('description') 
        phon.price = request.POST.get('price')           
        phon.quantity = request.POST.get('quantity')     
        phon.save()
        return redirect('phone_list')

    return render(request, 'update.html', {'phon': phon})


# DELETE 
def phone_delete(request, pk):
    phon = get_object_or_404(Phone, pk=pk)
    if request.method == "POST":
        phon.delete()
        return redirect('phone_list')
    return render(request, 'delete.html', {'phon': phon})


# DETAIL 
def phone_detail(request, pk):
    phon = get_object_or_404(Phone, pk=pk)
    return render(request, 'detail.html', {'phon': phon})



    