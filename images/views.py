from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm, Image
from django.shortcuts import get_object_or_404

@login_required
def image_create(request):
    """
    View for creating an Image using the Javascript Bookmarklet
    :param request:
    :return:
    """
    if request.method == 'POST':
        #form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            #form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            #assign current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            #redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        #build form with data provided by bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})

def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html', {'section': 'images', 'image': image})