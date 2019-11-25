import csv,io
from django.contrib import messages
from django.shortcuts import render
from .models import *
from .forms import ContactForm
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from urllib.parse import unquote

def index(request):
    return render(request,'restaurant_app/base.html')

def menu(request):
    category_list=[x[0] for x in Item.categories_choices]
    context = {'categories': category_list}
    return render(request,'restaurant_app/menu.html', context)

def contact(request):
    form=ContactForm()
    contact=Contact.objects.all()
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            print('ERROR FROM INVALID')
    return render(request,'restaurant_app/contact.html',{'form':form})

def order_pickup(request):
    return render(request,'restaurant_app/order_pickup.html')

def about(request):
    return render(request,'restaurant_app/about.html')

def food_items(request, section):
    category_list=[x[0] for x in Item.categories_choices]
    if section not in category_list:
        return HttpResponseRedirect('/menu')
    next_section_idx = (category_list.index(section) +1 ) % len(category_list)
    items_list=Item.objects.filter(category=section)
    context={'items_list':items_list, 'section':section , 'next_section': category_list[next_section_idx] }
    return render(request,'restaurant_app/food_items.html',context)

@permission_required('admin.can_add_log_entry')
def form_upload(request):
    #template="restaurant_app/form_upload.html"
    prompt={'order': 'item,item_description,category'}
    if request.method=="GET":
        return render(request,'restaurant_app/form_upload.html',prompt)


    csv_file=request.FILES['file']
    print("******",type(csv_file))
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')
    data_set= csv_file.read().decode('UTF-8')
    io_string=io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string,delimiter=',',quotechar='|'):
        _, created= Item.objects.update_or_create(
            item=column[0],
            item_description=column[1],
            category=column[2]

        )
    context={}
    return render(request,'restaurant_app/form_upload.html',context)
