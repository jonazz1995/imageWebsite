from django.shortcuts import render
from .models import Image

# View to display the gallery page
def gallery(request):
    # Retrieve all images from the database
    images = Image.objects.all()

    # Pass the images to the template
    return render(request, 'gallery/gallery.html', {'images': images})
