from main import db
from models.customer import Customer


class CustomerService:
    def __init__(self):
        pass

    def get_by_id(self, customer_id):
        return Customer.query.get(customer_id).all()

    def get_by_username(self, name):
        # Get customer by name from the database
        # Return Customer object if found, None otherwise
        pass

    def get_customers(self):
        customers = Customer.query.all()
        return customers

    def get_customer(self, customer_id):
        return self.get_by_id(customer_id)

    def register_customer(self, request_data):
        customer = Customer(
            name=request_data["name"],
            password=request_data["password"],
            correspondence_address=request_data["correspondence_address"],
            billing_cycle=request_data["billing_cycle"],
            email=request_data["email"],
            phone_number=request_data["phone_number"]
        )
        db.session.add(customer)
        db.session.commit()

    def update_customer_details(self, request_data):
        customer_id = request_data["customer_id"]
        customer = self.get_by_id(customer_id)
        if not customer:
            return {'success': False, "message": "Customer not found"}

        if "correspondence_address" in request_data:
            customer.correspondence_address = request_data["correspondence_address"]

        if "billing_cycle" in request_data:
            customer.billing_cycle = request_data["billing_cycle"]

        db.session.commit()
        return {'success': True, 'message': 'Profile updated successfully'}

    def delete_customer_details(self, request_data):
        customer_id = request_data["customer_id"]
        customer = self.get_by_id(customer_id)
        if not customer:
            return {'success': False, "message": "Customer not found"}

        db.session.delete(customer)
        db.session.commit()
        return {'success': True, 'message': 'Customer deleted successfully'}
