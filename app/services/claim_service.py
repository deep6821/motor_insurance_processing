from main import db
from models.claim import Claim


class ClaimService:
    def __init__(self):
        pass

    def get_by_id(self, claim_id):
        return Claim.query.get(claim_id).all()

    def submit_claim(self, request_data):
        claim = Claim(
            customer_id=request_data["customer_id"],
            claim_data=request_data["claim_data"],
            claim_status=request_data["claim_status"],
            claim_coverage=request_data["claim_coverage"],
            claim_amount=request_data["claim_amount"],
            claim_date=request_data["claim_date"]
        )
        db.session.add(claim)
        db.session.commit()

    def update_claim(self, request_data):
        claim_id = request_data["claim_id"]
        claim = self.get_by_id(claim_id)
        if not claim:
            return {'success': False, "message": "Claim not found"}

        if "claim_data" in request_data:
            claim.claim_data = request_data["claim_data"]

        db.session.commit()
        return {'success': True, 'message': 'Claim updated successfully'}

    def get_claim_status(self, claim_id):
        claim = self.get_by_id(claim_id)
        if claim:
            return {'success': True, 'message': 'Claim found', 'status': claim.status}
        else:
            return {'success': False, 'message': 'Claim not found'}

    def generate_claim_report(self, claim_id):
        claim = self.get_by_id(claim_id)
        if claim:
            # Generate report logic
            report = f"Report for claim {claim_id}"
            return {'success': True, 'message': 'Report generated', 'report': report}
        else:
            return {'success': False, 'message': 'Claim not found'}
