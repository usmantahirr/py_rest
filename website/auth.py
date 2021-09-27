from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        return email
    return render_template('signup.html')


@auth.route('/destroy')
def destroy():
    return "<h2>This isn't the right way but destroyed</h2>"
