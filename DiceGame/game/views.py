from django.shortcuts import render
from .models import Image
import random


def random_image(request):
    images = Image.objects.all()
    if images:
        dice1 = random.choice(images)
        dice2 = random.choice(images)
    else:
        dice1 = None
        dice2 = None

    if dice1 and dice2:
        if dice1.description > dice2.description:
            comparison_result = f"Player 1 !!!"
        elif dice1.description < dice2.description:
            comparison_result = f"Player 2 !!!"
        else:
            comparison_result = "It's a Draw!!!."
    else:
        comparison_result = "No images available for comparison."
        
    return render(request, 'images/random_image.html', {'dice1': dice1, 'dice2': dice2, 'comparison_result': comparison_result,})
