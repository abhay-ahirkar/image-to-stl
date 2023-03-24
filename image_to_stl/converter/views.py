from django.shortcuts import render
from .models import Image, STL

def index(request):
    if request.method == 'POST':
        image = Image(image=request.FILES['image'])
        image.name = image.image.name
        image.save()
        # Convert the image to an STL file here
        stl = STL()
        stl.name = image.name.split('.')[0] + '.stl'
        stl.save()
        return render(request, 'converter/index.html', {'stl': stl})
    else:
        return render(request, 'converter/index.html')
