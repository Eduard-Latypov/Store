from django.db.models import Q

from .models import Products


def q_search(query):
    if query.isdigit() and len(query) < 5:
        return Products.objects.filter(pk=int(query))

    q_objects = Q()

    for item in (word for word in query.split() if len(word) > 2):
        q_objects |= Q(name__icontains=item)
        q_objects |= Q(description__icontains=item)

    return Products.objects.filter(q_objects)
