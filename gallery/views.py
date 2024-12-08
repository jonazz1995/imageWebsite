from django.shortcuts import render
from .models import Image


def index_view(request):
    return render(request, 'index.html')


# View to display the gallery page
def portfolio(request):
    # Retrieve all images from the database
    images = Image.objects.all()

    # Pass the images to the template
    return render(request, "index.html", {"images": images})
