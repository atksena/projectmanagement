from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ExampleView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
