from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import BlogSerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Blog
from django.core.paginator import Paginator

class PublicBlogView(APIView):
    def get(self,request):
        try:

            blogs=Blog.objects.all().order_by("?")
            serializer=BlogSerializer(blogs,many=True)
            if request.GET.get('search'):
                search=request.GET.get('search')
                blogs=Blog.objects.filter(Q(title__icontains=search)|Q(blog_text__icontains=search))
            page_number=request.GET.get('page',1)
            pagiantor=Paginator(blogs,1)
            serializer=BlogSerializer(pagiantor.page(page_number),many=True)
            return Response({
                'data':serializer.data,
                'message':'Blogs fetched',
                'status':status.HTTP_200_OK
            })
        except Exception as e:
            return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request):
        try:
            blogs=Blog.objects.all()
            serializer=BlogSerializer(blogs,many=True)
            if request.GET.get('search'):
                search=request.GET.get('search')
                blogs=Blog.objects.filter(Q(title__icontains=search)|Q(blog_text__icontains=search))
            return Response({
                'data':serializer.data,
                'message':'Blogs fetched',
                'status':status.HTTP_200_OK
            })
        except Exception as e:
            return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        try:
            data=request.data
            data['user']=request.user.id
            
            serializer=BlogSerializer(data=data)
            if not serializer.is_valid():
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({
                'data':serializer.data,
                'message':'Blog Created',
                'status': status.HTTP_201_CREATED})
            return Response()
        except Exception as e:
            return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        try:
            data=request.data
            blog=Blog.objects.filter(uid=data.get('uid'))
            
            if not blog.exists():
                return Response({
                    'data':{},
                    'message':'Blog does not exist'
                },status=status.HTTP_400_BAD_REQUEST)
            if request.user!=blog[0].user:
                return Response({
                    'data':{},
                    'message':'You are not authorized to update this blog'
                },status=status.HTTP_401_UNAUTHORIZED)
            serializer=BlogSerializer(blog[0],data=data,partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({
                'data':serializer.data,
                'message':'Blog Update Successfully',
                'status': status.HTTP_201_CREATED})
            return Response()
        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        try:
            data=request.data
            blog=Blog.objects.filter(uid=data.get('uid'))
            
            if not blog.exists():
                return Response({
                    'data':{},
                    'message':'Blog does not exist'
                },status=status.HTTP_400_BAD_REQUEST)
            if request.user!=blog[0].user:
                return Response({
                    'data':{},
                    'message':'You are not authorized to update this blog'
                },status=status.HTTP_401_UNAUTHORIZED)
            serializer=BlogSerializer(blog[0],data=data,partial=True)
            blog[0].delete()
            return Response({
                'data':{},
                'message':'Blog Deleted Successfully',
                'status': status.HTTP_200_OK})
        except Exception as e:
            print(e)
            return Response({
                'data':{},
                'message':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)