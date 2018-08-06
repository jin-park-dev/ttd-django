from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from lists.models import Item, List
from lists.forms import ItemForm


# Create your views here.

# def home_page(request):
#     if request.method == 'POST':
#         item = Item()
#         item.text = request.POST.get('item_text', '')
#         item.save()
#         return render(request, 'home.html', {
#             'new_item_text': item.text,
#         })
#     return render(request, 'home.html')


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': error})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST.get('text'), list=list_)
    try:
        item.full_clean()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    # return redirect('view_list', list_.id) # If I don't have get_absolute_url in models use this
    return redirect(list_)
