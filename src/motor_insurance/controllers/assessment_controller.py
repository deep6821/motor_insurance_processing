from motor_insurance.services.assessment_service import AssessmentService


class AssessmentController:
    def __init__(self, db):
        self.db = db
        self.assessment_service = AssessmentService(self.db)

    def submit_assessment_report(self, claim_id, assessment_data):
        # Submit an assessment report for a claim
        assessment = self.assessment_service.create_assessment(
            claim_id, assessment_data
        )
        return {"success": True, "message": "Assessment report submitted successfully"}

    def approve_claim(self, claim_id):
        # Approve a claim
        assessment = self.assessment_service.get_by_claim_id(claim_id)
        if assessment:
            # Approve claim logic
            return {"success": True, "message": "Claim approved"}
        else:
            return {"success": False, "message": "Assessment report not found"}

    def reject_claim(self, claim_id):
        # Reject a claim
        assessment = self.assessment_service.get_by_claim_id(claim_id)
        if assessment:
            # Reject claim logic
            return {"success": True, "message": "Claim rejected"}
        else:
            return {"success": False, "message": "Assessment report not found"}
