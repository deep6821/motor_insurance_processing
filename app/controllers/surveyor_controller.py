from services.surveyor_service import SurveyorService


class SurveyorController:
    def __init__(self):
        self.surveyor_service = SurveyorService()

    def assign_case(self, case_id, surveyor_id):
        # Assign a case to a surveyor
        surveyor = self.surveyor_service.get_by_id(surveyor_id)
        if surveyor:
            # Assign case logic
            return {'success': True, 'message': 'Case assigned to surveyor'}
        else:
            return {'success': False, 'message': 'Surveyor not found'}

    def submit_assessment_report(self, case_id, assessment_data):
        # Submit an assessment report for a case
        surveyor = self.surveyor_service.get_by_case_id(case_id)
        if surveyor:
            # Submit assessment report logic
            return {'success': True, 'message': 'Assessment report submitted'}
        else:
            return {'success': False, 'message': 'Surveyor not found'}
