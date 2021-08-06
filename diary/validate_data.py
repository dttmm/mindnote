from .models import Page
import random


def validate_pages():
    pages = Page.objects.all()
    for page in pages:
        score = page.score
        if score < 0 or score > 10:
            value = random.randint(0, 10)
            page.score = value
            page.save()
