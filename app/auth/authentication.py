from models.customer import Customer


def authenticate(name, password):
    # Authenticate the user against the database
    user = Customer.query.filter_by(name=name).first()
    if user and user.password == password:
        return user
    return None


def generate_token(user):
    # import jwt
    # Generate an authentication token for the user
    # token_payload = {
    #     'user_id': user.id,
    #     'username': user.username
    #     # Add any additional payload data as needed
    # }
    # secret_key = 'your_secret_key'  # Replace with your own secret key
    # token = jwt.encode(token_payload, secret_key, algorithm='HS256')
    # return token.decode('utf-8')
    return 'your_generated_token'


def validate_token(token):
    # Validate the authentication token
    return True if token == 'your_generated_token' else False
