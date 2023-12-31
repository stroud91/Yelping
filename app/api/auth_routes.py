from flask import Blueprint, jsonify, session, request
from app.models import User, db
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from .aws import get_unique_filename, upload_file_to_s3


auth_routes = Blueprint('auth', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{error}')
    return errorMessages


@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': ['Unauthorized']}


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()

    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    print("Request data:", request.form)

    if form.validate_on_submit():
        image = request.files.get("profile_image_id")

        if image is not None:
            image.filename = get_unique_filename(image.filename)
            upload = upload_file_to_s3(image)
            print(upload)

            if "url" not in upload:
                print("Upload Error:", upload)
                return {'errors': ['Upload failed']}, 400

            user = User(
                username=form.data['username'],
                email=form.data['email'],
                password=form.data['password'],
                first_name=form.data['first_name'],
                last_name=form.data['last_name'],
                profile_image_id=upload["url"]
            )

            db.session.add(user)
            db.session.commit()
            login_user(user)
            return user.to_dict()

    print("Form Validation Errors:", form.errors)
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
