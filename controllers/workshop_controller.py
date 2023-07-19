from services.workshop_service import WorkshopService


class WorkshopController:
    def __init__(self):
        self.workshop_service = WorkshopService()

    def select_workshop(self, workshop_id):
        # Select a workshop for repairs
        workshop = self.workshop_service.get_by_id(workshop_id)
        if workshop:
            return {'success': True, 'message': 'Workshop selected', 'workshop_data': workshop.workshop_data}
        else:
            return {'success': False, 'message': 'Workshop not found'}

    def schedule_appointment(self, workshop_id, appointment_data):
        # Schedule an appointment with a workshop
        workshop = self.workshop_service.get_by_id(workshop_id)
        if workshop:
            # Schedule appointment logic
            return {'success': True, 'message': 'Appointment scheduled'}
        else:
            return {'success': False, 'message': 'Workshop not found'}

    def track_repair_progress(self, claim_id):
        # Track the repair progress of a claim
        workshop = self.workshop_service.get_by_claim_id(claim_id)
        if workshop:
            # Track repair progress logic
            return {'success': True, 'message': 'Repair progress tracked'}
        else:
            return {'success': False, 'message': 'Workshop not found'}
