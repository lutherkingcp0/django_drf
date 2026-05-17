from django.shortcuts import render # pyright: ignore[reportMissingModuleSource]
from rest_framework import  generics # pyright: ignore[reportMissingImports]
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.response import Response # pyright: ignore[reportMissingImports]
from rest_framework import status # pyright: ignore[reportMissingImports]
from rest_framework.views import APIView # pyright: ignore[reportMissingImports]
# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all() # pyright: ignore[reportUndefinedVariable]
    serializer_class = BlogPostSerializer # pyright: ignore[reportUndefinedVariable]

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete() # pyright: ignore[reportUndefinedVariable]
        return Response(status=status.HTTP_204_NO_CONTENT) # pyright: ignore[reportUndefinedVariable]
    
class BlogPostUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all() # pyright: ignore[reportUndefinedVariable]
    serializer_class = BlogPostSerializer # pyright: ignore[reportUndefinedVariable]
    lookup_field = 'pk'

class BlogPostList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get('title', "")

        if title:
            blogposts = BlogPost.objects.filter(title__icontains=title) # pyright: ignore[reportUndefinedVariable]
        else:
            blogposts = BlogPost.objects.all() # pyright: ignore[reportUndefinedVariable]

        serializer = BlogPostSerializer(blogposts, many=True) # pyright: ignore[reportUndefinedVariable]
        return Response(serializer.data) # pyright: ignore[reportUndefinedVariable]