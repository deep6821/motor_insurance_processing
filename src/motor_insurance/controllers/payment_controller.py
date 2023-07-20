from motor_insurance.services.payment_service import PaymentService


class PaymentController:
    def __init__(self, db):
        self.db = db
        self.payment_service = PaymentService(self.db)
        self.db = db

    def generate_payment_request(self, claim_id):
        # Generate a payment request for a claim
        payment = self.payment_service.create_payment(claim_id)
        return {
            "success": True,
            "message": "Payment request generated",
            "payment_id": payment.payment_id,
        }

    def process_payment(self, payment_data):
        # Process a payment
        payment = self.payment_service.get_by_payment_data(payment_data)
        if payment:
            # Process payment logic
            return {"success": True, "message": "Payment processed"}
        else:
            return {"success": False, "message": "Payment not found"}

    def check_payment_status(self, claim_id):
        # Check the payment status for a claim
        payment = self.payment_service.get_by_claim_id(claim_id)
        if payment:
            # Check payment status logic
            return {
                "success": True,
                "message": "Payment status checked",
                "status": payment.status,
            }
        else:
            return {"success": False, "message": "Payment not found"}
