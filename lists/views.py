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

#A Helper Method for Several Short Tests
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            # Item.objects.create(text=request.POST['text'], list=list_)
            form.save(for_list=list_)
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        # Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})
    # try:
    #     item.full_clean()
    # except ValidationError:
    #     list_.delete()
    #     error = "You can't have an empty list item"
    #     return render(request, 'home.html', {"error": error})
    # return redirect('view_list', list_.id) # If I don't have get_absolute_url in models use this
    # return redirect(list_)
