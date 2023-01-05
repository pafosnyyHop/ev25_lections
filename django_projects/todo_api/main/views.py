# from .models import Task
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from . import serializers
#
# # 'GET',    'POST',     'PUT',     'PATCH',            'DELETE'
# # list       create     update     partial_update       destroy
# # retrieve
#
# @api_view(['GET'])
# def tasks_list(request):
#     queryset = Task.objects.all()
#     serializer = serializers.TaskListSerializer(queryset, many=True)
#     return Response(serializer.data, status=200)
#
#
# @api_view(['GET'])
# def task_detail(request, id):
#     try:
#         task = Task.objects.get(id=id)
#         serializer = serializers.TaskDetailSerializer(task)
#         return Response(serializer.data, status=200)
#     except Task.DoesNotExist:
#         return Response(f'Does not exist this task {id} id!', status=404)
#
#
# @api_view(['POST'])
# def task_create(request):
#     # print(request.data, '!!!!!!!')
#     # print('!!!!!!!!!!')
#     # print(dir(request))
#     serializer = serializers.TaskDetailSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=201)
#
#
# @api_view(['PUT', 'PATCH'])
# def task_update(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#         if request.method == 'PUT':
#             serializer = serializers.TaskDetailSerializer(instance=task, data=request.data)
#         else:
#             serializer = serializers.TaskDetailSerializer(instance=task, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=206)
#     except Task.DoesNotExist:
#         return Response(f'Does not exist this task {pk} id!', status=404)
#
#
# @api_view(['DELETE'])
# def task_delete(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#         task.delete()
#         return Response({'msg': 'Deleted Successfully'}, status=204)
#     except Task.DoesNotExist:
#         return Response(f'Does not exist this task {pk} id!', status=404)


from django.http import Http404

from .models import Task
from rest_framework.decorators import api_view
from . import serializers
from rest_framework import generics

# function based-view

# Class-based views
# 3 вида:
# Api View, Generics, ViewSet


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.TaskListSerializer
        return serializers.TaskDetailSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATH'):
            return serializers.T





















# class TaskListCreateApiView(APIView):
#     def get(self, request):
#         queryset = Task.objects.all()
#         serializer = serializers.TaskListSerializer(instance=queryset, many=True)
#         return Response(serializer.data, status=200)
#
#     def post(self, request):
#         serializer = serializers.TaskDetailSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)
#
#
# class TaskDetailApiView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Task.objects.get(id=pk)
#         except Task.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         queryset = self.get_object(pk)
#         try:
#             serializer = serializers.TaskDetailSerializer(queryset)
#             return Response(serializer.data, status=200)
#         except:
#             return Response(f'Does not exist this task with {pk} id!', status=404)
#
#     def put(self, request, pk):
#         queryset = self.get_object(pk)
#         serializer = serializers.TaskDetailSerializer(instance=queryset, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
#
#     def delete(self, request, pk):
#         queryset = self.get_object(pk)
#         queryset.delete()
#         return Response({'msg': 'Successfully deleted!'}, status=204)











