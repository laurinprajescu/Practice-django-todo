# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from todo.serializers import TodoSerializer
from todo.models import Todo


class TodoView(APIView):
    """
    TodoView used to handle the incoming requests relating to
    `todo` items
    """

    def get(self, request):
        """
        Handle the GET request for the `/todo/` endpoint.

        Retrieve a complete list of `todo` items from the Todo
        model, serialize them to JSON and return the serialized
        todo items.

        Returns the serialized `todo` objects.
        """
        todo_items = Todo.objects.all()
        # Serialize the data retrieved from the DB and serialize
        # them using the `TodoSerializer`
        serializer = TodoSerializer(todo_items, many=True)
        # Store the serialized data `serialized_data`
        serialized_data = serializer.data
        return Response(serialized_data)

    def post(self, request):
        """
        Handle the POST request for the `/todo/` endpoint.

        This view will take the `data` property from the `request` object,
        deserialize it into a `Todo` object and store in the DB.

        Returns a 201 (successfully created) if the item is successfully
        created, otherwise returns a 400 (bad request)
        """
        serializer = TodoSerializer(data=request.data)

        # Check to see if the data in the `request` is valid.
        # If the cannot be deserialized into a Todo object then
        # a bad request respose will be returned containing the error.
        # Else, save the data and return the data and a successfully
        # created status
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
