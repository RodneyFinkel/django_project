# from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response #instead of JsonResponse
from .serializers import ProjectSerializer
from saas_app.models import Project, Review


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},
        
        {'POST': '/api/user/token'},
        {'POST': '/api/user/token/refresh'},
    ]

    return Response(routes)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    print('USER:', request.user)
    projects = Project.objects.all()
    #serializer is an object/instance of ProjectSerializer so we need to extract the data using .data (which is a method of the 
    # ProjectSerializer Class)
    serializer = ProjectSerializer(projects, many=True) # serializer = ProjectSerializer(project, many=False).data    ALTERNATIVE
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)  
    serializer = ProjectSerializer(project, many=False)   
    return Response(serializer.data)


# The following view is for a review vote

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile   # User is being extracted from Token not sessionID
    data = request.data
    print('DATA:', data)
    review, created = Review.objects.get_or_create(
        owner = user,
        project = project,

    )
    review.value = data['value']
    review.save()
    project.getVoteCount

    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)