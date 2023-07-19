from models.payment import Payment


class PaymentService:
    def __init__(self):
        pass

    def create_payment(self, claim_id):
        # Create a new payment record in the database
        # Return Payment object
        pass

    def get_by_payment_data(self, payment_data):
        # Get payment by payment data from the database
        # Return Payment object if found, None otherwise
        pass

    def get_by_claim_id(self, claim_id):
        # Get payment by claim ID from the database
        # Return Payment object if found, None otherwise
        pass
