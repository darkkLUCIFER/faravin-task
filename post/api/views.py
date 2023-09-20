from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from extensions.permissions import IsCreatorOrReadOnly
from post.api.serializers import PostSerializer
from post.models import Post


class PostView(APIView):
    """
        get:
            return list of all user posts or just one post with given pk

            parameter: [post_id]

        post:
            create new post

            body: [title, description]

        put:
            update data of a post

            body: [title, description]

        delete:
            remove a specific post

            parameter: [pk]
    """
    permission_classes = [IsCreatorOrReadOnly]

    def get(self, request):
        user = self.request.user
        post_id = self.request.query_params.get('post_id')
        try:
            post = Post.objects.get(id=post_id, user=user)
        except Post.DoesNotExist:
            post = None
        if post:
            serializer = PostSerializer(post)
            return Response(
                serializer.data
            )
        else:
            return Response(
                {
                    'error': 'post not found'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        user = self.request.user
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            description = serializer.data.get('description', None)

            Post.objects.create(
                user=user,
                title=title,
                description=description
            )
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors
            )

    def put(self, request):
        user = self.request.user
        post_id = self.request.query_params.get('post_id')
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            try:
                post = Post.objects.get(id=post_id, user=user)
            except Post.DoesNotExist:
                post = None
            if post:
                fields_to_update = ['title', 'description']
                for field in fields_to_update:
                    if serializer.data.get(field):
                        setattr(post, field, serializer.data.get(field))
                    post.save()

                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'error': 'post not found'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                serializer.errors
            )

    def delete(self, request):
        user = self.request.user
        post_id = self.request.query_params.get('post_id')
        try:
            post = Post.objects.get(id=post_id, user=user)
        except Post.DoesNotExist:
            post = None
        if post:
            post.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {
                    'error': 'post not found'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
