from django.db.models import Q
from .models import Profile, Skill


def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    print('SEARCH:', search_query)

    skills = Skill.objects.filter(name__iexact=search_query)

    profiles = Profile.objects.distinct().filter(
     Q(name__icontains=search_query) | 
     Q(short_intro__icontains=search_query) |
     Q(skill__in=skills)
     )
    return profiles, search_query

# SEARCH FEATURES IN TAKEN FROM  profiles(request) views in views.py
# Icontains makes sure the parameter passed is not case sensitive
# Using filter() method instead of get() method
# profile view is also being used for the search utility here in 
#  profile=Profile.object.filter(name_icontains=search_query)
# from django.db.models import Q
# Profile.objects.filter(Q(name__icontains=search_query), 
        # Q(short_intro__icontains=search_query))
# Q-modules used to pass two parameters with an or value in order to have the 
# search filter look both in the name and and short_intro fields
# all of this has now been taken to the utils.py file