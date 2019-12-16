from flask import Blueprint, render_template, abort, request, url_for, redirect
from flask_login import login_required, login_user, current_user, logout_user
from jinja2 import TemplateNotFound
import user_form
from models import User, db
user = Blueprint('user', __name__,
                        template_folder='templates')

@user.route('/register', methods=['GET', 'POST'])
def register():
    register_form = user_form.RegisterForm()
    if request.method == 'POST' and register_form.submit and register_form.validate_on_submit():
        new_user = User(register_form.username.data, register_form.email.data, register_form.password.data, register_form.fullname.data )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('user.login'))
    return render_template('user/register.html', form = register_form)

@user.route('/login', methods=['GET', 'POST'])
def login():
    login_form = user_form.LoginForm()
    if request.method == 'POST' and login_form.submit and login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        login_user(user)
        return redirect(url_for('index'))
    return render_template('user/login.html', form=login_form)

@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))