## Design an electronic claims processing for vehicle insurance using Python with TDD approach

### Dependencies:
You just need `Python`.Visit the link [python official link](https://www.python.org/downloads) to install Python.

### Description:
This repository gives an overview of how we can design an electronic claims processing for vehicle insurance.

### Project setup:
1. Activate virtual env
2. Make source root directory as: C:\office\rohit-workspace\motor_insurance_processing\src
3. Export:
   1. Windows: $env:PYTHONPATH = "C:\office\rohit-workspace\motor_insurance_processing\src"
   OR set PYTHONPATH=C:\office\rohit-workspace\motor_insurance_processing\src
   2. 
     cd motor_insurance
     set FLASK_APP=app.py
     echo %FLASK_APP%
4. For running migrations:
   1. flask db init
   2. flask db migrate -m "Initial migration"
   3. flask db upgrade

### Directory Structure:
```
└───src
    └───motor_insurance
        ├───auth
        ├───controllers
        ├───migrations
        │   └───versions
        ├───models
        └───services
```
### File Description:
```

```


### Example: To run Flask application
```
flask run
```

### To run test cases
```

```



