from . models import Vendor_details, Purchase_Order,Performance_Model
from .serializers import (
    Vendor_detail_serializers,
    update_vendor_details, 
    purchase_order_serializer,
    Purchase_order_update_serializer,
    Vendor_Performance_Serializer)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
# Create your views here.


@api_view(['POST'])  
def create_vendor(request):
    vendor_post_details = Vendor_detail_serializers(data=request.data)
    if vendor_post_details.is_valid():
        vendor_post_details.save()
        return Response(vendor_post_details.data, status=status.HTTP_201_CREATED)
    else:
        return Response(vendor_post_details.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])   
def list_vendors(request):
    vendors_data = Vendor_details.objects.all()
    vendors_list=Vendor_detail_serializers(vendors_data,many=True)
    return Response(vendors_list.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def Vendor_Details_By_Id(request,id):
    try:
        Particular_Vendor_details = Vendor_details.objects.get(id=id)
        serialized_data= Vendor_detail_serializers(Particular_Vendor_details)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    except Vendor_details.DoesNotExist:
        return Response("Vendor Not Found", status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def Vendor_Details_Update_By_Id(request,id):
    try:
       particular_vendor_details = Vendor_details.objects.get(id=id)
       Updated_vendor_data = update_vendor_details(instance=particular_vendor_details,data=request.data)
       if Updated_vendor_data.is_valid():
            Updated_vendor_data.save()
            updated_details = Vendor_detail_serializers(instance=particular_vendor_details)
            return Response(updated_details.data, status=status.HTTP_200_OK)
       else:
            return Response(updated_details.errors, status=status.HTTP_400_BAD_REQUEST)
    except Vendor_details.DoesNotExist:
        return Response("Vendor Not Found", status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['DELETE'])
def Vendor_Delete_By_Id(request,id):
    try:
        particular_vendor_data= Vendor_details.objects.get(id=id)
        particular_vendor_data.delete()
        return Response("VENDOR DELETED", status=status.HTTP_200_OK)
    except Vendor_details.DoesNotExist:
        return Response("Venodr Doesn't Exists", status=status.HTTP_204_NO_CONTENT)
    
                       #### for purchase orders ####

@api_view(['GET'])
def purchase_order_details(request):
    model_date = Purchase_Order.objects.all()
    serializer = purchase_order_serializer(model_date, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def Purchase_Order_Create(request):
    Serlialized_data = purchase_order_serializer(data=request.data)
    
    if Serlialized_data.is_valid():
        Serlialized_data.save()
        return Response("Purchase Order created successfully", status=status.HTTP_201_CREATED)
    else:
        return Response(Serlialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def Purchase_order_Details_Update(request,id):
    try:
        particular_po_data = Purchase_Order.objects.get(id=id)
        Updated_po_data =Purchase_order_update_serializer(instance=particular_po_data, data=request.data)
        if Updated_po_data.is_valid():
            Updated_po_data.save()
            response = purchase_order_serializer(instance=particular_po_data)
            return Response(response.data, status=status.HTTP_200_OK)
        else:
            return Response(Updated_po_data.errors, status=status.HTTP_401_UNAUTHORIZED)
    except Purchase_Order.DoesNotExist:
        return Response("purchase order is not found",status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def Purchase_order_Details_By_id(request,id):
    try:
        particular_po_data = Purchase_Order.objects.get(id=id)
        po_details = purchase_order_serializer(particular_po_data, many=False)
        return Response(po_details.data, status=status.HTTP_200_OK)
    except Purchase_Order.DoesNotExist:
        return Response("Purchase Order Not exists",status=status.HTTP_204_NO_CONTENT)
    
@api_view(['DELETE'])
def Purchase_order_Delete_By_Id(request,id):
    try:
        paticular_po_data=Purchase_Order.objects.get(id=id)
        paticular_po_data.delete()
        return Response(f"Porchase_Order of {id} is deleted",status=status.HTTP_204_NO_CONTENT)
    except:
        return Response('Purchase_Order not exist',status=status.HTTP_404_NOT_FOUND)
    

                              ### SETTING ACKNOWLDGMENT DATE ###
@api_view(['POST'])
def Acknowledgment_Update(request,id):
    try:
        model_data = Purchase_Order.objects.get(id=id)
        
        if model_data.status == 'completed' and model_data.delivery_date <=timezone.now().date():
            message = request.data.get("Acknowledgment_Message")
            if message:
                model_data.acknowledgment_date = timezone.now().date()
                model_data.save(update_fields=['acknowledgment_date'])
                return Response("Acknowledgment Recieved",status=status.HTTP_200_OK)
            else:
                return Response("Please provide a Acknowledgment Message",status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Purchase Order is Not deliverd Yet",status=status.HTTP_400_BAD_REQUEST)
    except Purchase_Order.DoesNotExist:
        return Response("Purchase Order is Not Found",status=status.HTTP_404_NOT_FOUND)
    
                          ### Vendor_Historical_Performance ###
@api_view(['GET'])
def vendor_performance_by_id(request,id):
    try:
        vendor_metrics = Vendor_details.objects.get(id=id)
        serializer_data = Vendor_Performance_Serializer(vendor_metrics,many=False)
        return Response(serializer_data.data, status=status.HTTP_200_OK)
    except Performance_Model.DoesNotExist:
        return Response("Vendor Id is not found", status=status.HTTP_204_NO_CONTENT)
    