from django.urls import path
from . import views

urlpatterns = [
               ### VENDOR_DETAILS_URLS ###
    path('vendors/', views.create_vendor),
    path('vendor_details', views.list_vendors),
    path('vendor_details/<int:id>',views.Vendor_Details_By_Id),
    path('vendor_update_by_id/<int:id>',views.Vendor_Details_Update_By_Id),
    path('vendor_delete_by_id/<int:id>',views.Vendor_Delete_By_Id),
           
                ### PURCHASE_ORDER_URLS ###
    path('purchase_order_details', views.purchase_order_details),
    path('purchase_order_create', views.Purchase_Order_Create),
    path('Edit_purchase_order_details/<int:id>', views.Purchase_order_Details_Update),
    path('purchase_order_detils/<int:id>',views.Purchase_order_Details_By_id),
    path('Delete_By_Id/<int:id>',views.Purchase_order_Delete_By_Id),
    path("purchase_orders_acknowledgment/<int:id>/acknowledge",views.Acknowledgment_Update),
      
                ### VENDOR_METRICS_URLS ###
    path('vendors/<int:id>/performance',views.vendor_performance_by_id)

]