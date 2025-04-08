import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Configure logging for diagnostics
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

@api_view(['GET'])
def api_root(request, format=None):
    logger.debug("api_root endpoint accessed")
    base_url = 'https://fuzzy-space-guacamole-w57w9vqp7x29p57-8000.app.github.dev/'
    return Response({
        'users': base_url + 'api/users/',
        'teams': base_url + 'api/teams/',
        'activities': base_url + 'api/activities/',
        'leaderboard': base_url + 'api/leaderboard/',
        'workouts': base_url + 'api/workouts/',
    })

@api_view(['GET'])
def users(request):
    logger.debug("users endpoint accessed")
    return Response({"message": "Users endpoint placeholder"})

@api_view(['GET'])
def teams(request):
    logger.debug("teams endpoint accessed")
    return Response({"message": "Teams endpoint placeholder"})

@api_view(['GET'])
def activities(request):
    logger.debug("activities endpoint accessed")
    return Response({"message": "Activities endpoint placeholder"})

@api_view(['GET'])
def leaderboard(request):
    logger.debug("leaderboard endpoint accessed")
    return Response({"message": "Leaderboard endpoint placeholder"})

@api_view(['GET'])
def workouts(request):
    logger.debug("workouts endpoint accessed")
    return Response({"message": "Workouts endpoint placeholder"})