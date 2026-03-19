# from django.shortcuts import render
# from watchlist_app.models import *
# from django.http import JsonResponse
# from django.shortcuts import render, get_object_or_404
# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     # Turn the QuerySet of dictionaries into a standard Python list
#     data = {
#         "movies": list(movies.values()) 
#     }
#     return JsonResponse(data)

# def movie_detail(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     data = { "name": movie.name,
#             "description": movie.description
#     }
#     return JsonResponse(data)

