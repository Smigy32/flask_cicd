from flask import Blueprint, request, jsonify, render_template

from app.models import UserModel

user_bp = Blueprint('users', __name__)


@user_bp.route("/")
def index():
    return render_template("index.html")


@user_bp.route("/users/", methods=['GET'])
def get_users():
    email = request.args.get("email")
    users = UserModel.return_all()

    # a simple filter by email QUERY param
    if email:
        user = UserModel.find_by_email(email)
        return jsonify(user)

    return render_template("get_users.html", users=users)


@user_bp.route("/new/", methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form.get("name")
        age = request.form.get("age")
        email = request.form.get("email")
        password = request.form.get("password")

        if not name or not age or not email or not password:  # to add user you need to set all values
            return render_template("response.html",
                                   response="Please fill in all information about the user!"), 400

        if UserModel.find_by_email(email, to_dict=False):
            return render_template("response.html", response="User with same email already exists. "
                                                             "Try another one."), 409

        hashed_password = UserModel.generate_hash(password)
        user = UserModel(name=name, age=age, email=email, hashed_password=hashed_password)
        user.save_to_db()

        return render_template("response.html", response=f"User with email {email} has been created!"), 201

    return render_template("create_user.html")
