Main File Name: Vendor_Management_System

MyVenve--> Virtual Environment(activate it by using activate.bat command)

Project Name:VMS_PROJECT
App Name: For_Vendors

To install all the packages used in this project into your project:- pip install -r requirements. txt -->in the terminal

Vendor_Management_System\MyVenv\VMS_PROJECT\python manage.py runserver (To run the server)
All the functionality code written in views.py.
All the Rest Framework code written in serializers.py.
All the Database Models code writen in models.py.
All the Url End points written in urls.py.
All the logic code written in signals.py.

                                           API ENDPOINTS
1) FOR VENDOR PROFILE MANAGEMENT :-
      Create a new vendor :- http://127.0.0.1:8000/api/vendors/ (POST)
      List All Vendors    :- http://127.0.0.1:8000/api/vendor_details (GET)
Retrieve a specific Vendor :- http://127.0.0.1:8000/api/vendor_details/1 (GET)
Update a vendor details   :- http://127.0.0.1:8000/api/vendor_update_by_id/4 (PUT)
        Delete a vendor   :- http://127.0.0.1:8000/api/vendor_delete_by_id/5 (DELETE)


2) FOR PURCHASE ORDER TRACKING :-
       Create a purchase order   :- http://127.0.0.1:8000/api/purchase_order_create (POST)
        List all purchase orders  :- http://127.0.0.1:8000/api/purchase_order_details (GET)
Retrieve details of a specific po :- http://127.0.0.1:8000/api/purchase_order_detils/2 (GET)
 Update a purchase order    :- http://127.0.0.1:8000/api/Edit_purchase_order_details/1 (PUT)
        Delete a purchase order   :- http://127.0.0.1:8000/api/Delete_By_Id/2  (DELETE)

3) FOR VENDOR PERFORMANCE EVALUATION :-
Retrieve a vendor's performance metrics :- http://127.0.0.1:8000/api/vendors/3/performance (GET)

4) FOR ACKNOWLEDGMENT ENDPOINT :-
 vendors to acknowledge POs :- http://127.0.0.1:8000/api/purchase_orders_acknowledgment/1/acknowledge  (POST)

These are the endpoints. You can run them using POSTMAN or Swagger.
To Run the endpoints using postman:-
      Run the server using--> python manage.py runserver
      Copy paste the Endpoint Url In the postman URL BOX and set the HTTP method and send Request.

                                   
                                  For Backend Logic calculating Performance Metrics
All the logic to calculate the vendor metrics is written in the signals.py file. It run automatically whenever the changes happen.


                                                       



     

