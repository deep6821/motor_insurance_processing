from motor_insurance.services.claim_service import ClaimService


class ClaimController:
    def __init__(self, db):
        self.db = db
        self.claim_service = ClaimService(self.db)

    def submit_claim(self, request_data):
        # Create a new claim
        claim = self.claim_service.submit_claim(request_data)
        return {
            "success": True,
            "message": "Claim created successfully",
            "claim_id": claim.claim_id,
        }

    def update_claim(self, request_data):
        # Update an existing claim
        return self.update_claim(request_data)

    def get_claim_status(self, claim_id):
        # Get the status of a claim
        return self.claim_service.get_claim_status(claim_id)

    def generate_claim_report(self, claim_id):
        # Generate a report for a claim
        return self.claim_service.generate_claim_report(claim_id)
