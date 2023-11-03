from django.shortcuts import redirect, render
from .forms import ImageUploadForm
from .models import CustomerImage
from django.contrib import messages


def upload_file(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            customer_name = form.cleaned_data['customer_name']
            image = request.FILES['file']

            customer_image = CustomerImage(customer_name=customer_name, image=image)
            customer_image.save()

            return redirect('upload_success')
    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})


def upload_success(request):
    return render(request, 'upload_success.html')
