from services.case_service import CaseService


class CaseController:
    def __init__(self):
        self.case_service = CaseService()

    def assign_case(self, case_id, adjuster_id):
        # Assign a case to an adjuster
        case = self.case_service.get_by_id(case_id)
        if case:
            # Assign case logic
            return {'success': True, 'message': 'Case assigned to adjuster'}
        else:
            return {'success': False, 'message': 'Case not found'}

    def make_adjustments(self, case_id, adjustments):
        # Make adjustments to a case
        case = self.case_service.get_by_id(case_id)
        if case:
            # Make adjustments logic
            return {'success': True, 'message': 'Adjustments made to case'}
        else:
            return {'success': False, 'message': 'Case not found'}
