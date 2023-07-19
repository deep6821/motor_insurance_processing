from services.customer_service import CustomerService


class CustomerController:
    def __init__(self):
        self.customer_service = CustomerService()

    def authenticate_user(self, username, password):
        # Authenticate the user
        customer = self.customer_service.get_by_username(username)
        if customer and customer.password == password:
            return {'success': True, 'message': 'Authentication successful'}
        else:
            return {'success': False, 'message': 'Authentication failed'}

    def get_customers(self):
        customers = self.customer_service.get_customers()
        return customers

    def get_customer(self, customer_id):
        customer = self.customer_service.get_customer(customer_id)
        return customer

    def register_customer(self, request_data):
        self.customer_service.register_customer(request_data)

    def update_customer_details(self, request_data):
        # Update the customer profile
        return self.customer_service.update_customer_details(request_data)

    def delete_customer_details(self, request_data):
        # Update the customer profile
        return self.customer_service.delete_customer_details(request_data)
