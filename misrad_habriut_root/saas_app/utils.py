from django.db.models import Q
from .models import Tag, Project


# def searchApps(request):
#     search_query = ''

#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')

#     # filtering for tags because of tags' many to many relationship with apps/projects
#     tags = Tag.objects.filter(name__icontains=search_query)

#     # this section is the search functionality (.filter() instead of .get())
#     apps = Project.objects.distinct().filter(
#         Q(title__icontains=search_query) |
#         Q(description__icontains=search_query) |
#         Q(owner__name__icontains=search_query) |
#         Q(tags__in=tags)
#     )

#     return apps, search_query

