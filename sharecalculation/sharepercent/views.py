from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response


class DistributeView(GenericAPIView):
    def get(self, request):
        if not self.request.query_params:
            data = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "error": "Query parameters are required."
            }
            return Response(data)

        total_amount_value = self.request.query_params.get('total_amount', None)
        if not total_amount_value:
            data = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "error": "Total Amount is required."
            }
            return Response(data)

        l1 = self.request.query_params.dict()
        del l1['total_amount']

        if len(l1) % 2 != 0:
            data = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "error": "Each user should have respective share value."
            }
            return Response(data)

        share_sum = sum([float(val) for key, val in l1.items() if 'share' in key])

        total_share_per = 100
        if share_sum*100 > total_share_per:
            data = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "error": "Total amount can't be divided according to the given share percentage."
            }
            return Response(data)

        users = []
        shares = []
        for key, value in l1.items():
            if 'id' in key:
                users.append(value)
            if 'share' in key:
                shares.append(value)

        users_share = {}
        for i in range(0, len(shares)):
            users_share[users[i]] = str(float(shares[i]) * int(total_amount_value))

        data = {
            "status_code": status.HTTP_200_OK,
            "message": "Data Calculated",
            'total_amount': total_amount_value,
            "Shares": users_share
        }
        return Response(data)
