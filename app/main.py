from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from base import SessionLocal, Base
from auth.authentication import authenticate, generate_token, validate_token
from auth.authorization import authorize
from controllers.customer_controller import CustomerController
from controllers.claim_controller import ClaimController
from controllers.assessment_controller import AssessmentController
from controllers.payment_controller import PaymentController
from controllers.workshop_controller import WorkshopController
from controllers.surveyor_controller import SurveyorController
from controllers.case_controller import CaseController

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/rohit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app, model_class=Base)
db.session = SessionLocal()
migrate = Migrate(app, db)

customer_controller = CustomerController()
claim_controller = ClaimController()
assessment_controller = AssessmentController()
payment_controller = PaymentController()
workshop_controller = WorkshopController()
surveyor_controller = SurveyorController()
case_controller = CaseController()


@app.route('/welcome', methods=['GET'])
def welcome():
    return jsonify(
        greeting=["hello", "rohit"],
    )


# Protected endpoint
@app.route('/protected', methods=['GET'])
@authorize
def protected():
    return jsonify({'success': True, 'message': 'Protected endpoint'})


# Authentication endpoint
@app.route('/login', methods=['POST'])
def login():
    name = request.json.get('name')
    password = request.json.get('password')

    # Authenticate the user
    user = authenticate(name, password)
    if user:
        # Generate and return an authentication token
        token = generate_token(user)
        return jsonify({'success': True, 'message': 'Login successful', 'token': token}), 200
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401


@app.route("/customer", methods=["GET"])
def get_customers():
    customers = customer_controller.get_customers()
    return jsonify(customers), 200


@app.route("/customer/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = customer_controller.get_customer(customer_id)
    if not customer:
        return jsonify({"message": "Customer not found"}), 404
    return jsonify(customer), 200


@app.route("/customer/register", methods=["POST"])
def register_customer():
    request_data = request.json
    customer_controller.register_customer(request_data)
    return jsonify({"message": "Customer registered successfully"}), 200


@app.route('/customer/update/<int:customer_id>', methods=['POST'])
@validate_token
def update_customer_details():
    request_data = request.json
    customer = customer_controller.update_customer_details(request_data)
    if customer["success"]:
        return jsonify(customer), 200

    return jsonify(customer), 404


@app.route('/customer/update/<int:customer_id>', methods=['DELETE'])
def delete_customer_details():
    request_data = request.json
    customer = customer_controller.delete_customer_details(request_data)
    if customer["success"]:
        return jsonify(customer), 200

    return jsonify(customer), 404


# Claim endpoints
@app.route('/claim/submit', methods=['POST'])
@validate_token
def submit_claim():
    request_data = request.json()
    result = claim_controller.submit_claim(request_data)
    if result["success"]:
        return jsonify({"message": result["message"]}), 200

    return jsonify({"message": result["message"]}), 404


@app.route('/claim/update/<int:claim_id>', methods=['POST'])
@validate_token
def update_claim():
    request_data = request.json()
    result = claim_controller.update_claim(request_data)
    if result["success"]:
        return jsonify({"message": result["message"]}), 200

    return jsonify({"message": result["message"]}), 404


# Assessment endpoints
@app.route('/assessment/submit', methods=['POST'])
@validate_token
def submit_assessment_report():
    claim_id = request.form['claim_id']
    assessment_data = request.form['assessment_data']
    result = assessment_controller.submit_assessment_report(claim_id, assessment_data)
    return jsonify(result)


# Payment endpoints
@app.route('/payment/process', methods=['POST'])
@validate_token
def process_payment():
    payment_data = request.form['payment_data']
    result = payment_controller.process_payment(payment_data)
    return jsonify(result)


# Workshop endpoints
@app.route('/workshop/select', methods=['POST'])
@validate_token
def select_workshop():
    workshop_id = request.form['workshop_id']
    result = workshop_controller.select_workshop(workshop_id)
    return jsonify(result)


# Surveyor endpoints
@app.route('/surveyor/assign', methods=['POST'])
@validate_token
def assign_case_to_surveyor():
    case_id = request.form['case_id']
    surveyor_id = request.form['surveyor_id']
    result = surveyor_controller.assign_case(case_id, surveyor_id)
    return jsonify(result)


# Case endpoints
@app.route('/case/assign', methods=['POST'])
@validate_token
def assign_case_to_adjuster():
    case_id = request.form['case_id']
    adjuster_id = request.form['adjuster_id']
