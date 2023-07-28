## Design an electronic claims processing for vehicle insurance using Python with TDD approach

### Dependencies:
You just need `Python`.Visit the link [python official link](https://www.python.org/downloads) to install Python.

### Description:
This repository gives an overview of how we can design an electronic claims processing for vehicle insurance.

### Project setup:
1. Activate virtual env
2. Make source root directory as: C:\office\rohit-workspace\motor_insurance_processing\src
3. Install Python packages: pip install requirements.txt
4. Export:
   1. Windows: $env:PYTHONPATH = "C:\office\rohit-workspace\motor_insurance_processing\src"
   OR set PYTHONPATH=C:\office\rohit-workspace\motor_insurance_processing\src
   2. 
     cd motor_insurance
     set FLASK_APP=app.py
     echo %FLASK_APP%
5. For running migrations:
   1. flask db init
   2. flask db migrate -m "Initial migration"
   3. flask db upgrade

### Directory Structure:
```
- motor_insurance/
  - auth/
    - authentication.py
    - authorization.py
  - controllers/
    - accident_controller.py
    - adjustor_controller.py
    - assessment_controller.py
    - case_controller.py
    - case_manager_report_controller.py
    - claim_controller.py
    - customer_controller.py
    - document_controller.py
    - notification_controller.py
    - payment_controller.py
    - policy_controller.py
    - regional_manager_report_controller.py
    - service_station_controller.py
    - surveyor_controller.py
    - top_management_report_controller.py
    - workshop_controller.py

  - models/
    - accident.py
    - adjustor.py
    - assessment.py
    - case.py
    - case_manager_report.py
    - claim.py
    - customer.py
    - document.py
    - notification.py
    - payment.py
    - policy.py
    - regional_manager_report.py
    - service_station.py
    - surveyor.py
    - top_management_report.py
    - workshop.py

  - services/
    - assessment_service.py
    - case_service.py
    - claim_service.py
    - customer_service.py
    - payment_service.py
    - surveyor_service.py
    - workshop_service.py

  - alembic.ini
  - app.py
  - base.py
  - Dockerfile
  - requirements.txt
```
### File Description:
```

```


### Example: To run Flask application
```
flask run
```

### Example: To run Flask application using Docker
```
# Build the Docker image
docker build -t flask_app .

# Run the Docker container
docker run -p 5000:5000 flask_app

```

### To run test cases
```

```



