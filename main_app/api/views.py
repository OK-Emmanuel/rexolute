from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserListView(APIView):
    def get(self, request):
        # Retrieve the list of users
        return Response({'message': 'GET request to list users'}, status=status.HTTP_200_OK)
    

class UserDetailView(APIView):
    def get(self, request, id):
        # Retrieve the details of a specific user
        return Response({'message': f'GET request to get details of user with id {id}'}, status=status.HTTP_200_OK)

class TherapistListView(APIView):
    def get(self, request):
        # Retrieve the list of therapists
        return Response({'message': 'GET request to list therapists'}, status=status.HTTP_200_OK)   

class TherapistDetailView(APIView):
    def get(self, request, id):
        # Retrieve the details of a specific therapist
        return Response({'message': f'GET request to get details of therapist with id {id}'}, status=status.HTTP_200_OK)    

class PaymentListView(APIView):
    def get(self, request):
        # Retrieve the list of payments
        return Response({'message': 'GET request to list payments'}, status=status.HTTP_200_OK)    

class PaymentDetailView(APIView):    
    def get(self, request, id):
        # Retrieve the details of a specific payment
        return Response({'message': f'GET request to get details of payment with id {id}'}, status=status.HTTP_200_OK)

class SessionListView(APIView):
    def get(self, request):
        # Retrieve the list of sessions
        return Response({'message': 'GET request to list sessions'}, status=status.HTTP_200_OK)

class SessionDetailView(APIView):
    def get(self, request, id):
        # Retrieve the details of a specific session
        return Response({'message': f'GET request to get details of session with id {id}'}, status=status.HTTP_200_OK)