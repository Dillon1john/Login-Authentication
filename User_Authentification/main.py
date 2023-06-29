from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
# from flask_wtf import FlaskForm
# from wtforms import SubmitField, PasswordField, StringField
# from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)


# ## CREATE LOG IN FORM
# class LoginForm(FlaskForm):
#     email = StringField('Email',validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Let me in')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()



@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        password = request.form.get("password")
        hashed_password = generate_password_hash(password,
                                                 method="pbkdf2:sha256",
                                                 salt_length=8)
        new_user = User(email=request.form.get('email'),
                        name=request.form.get('name'),
                        password=hashed_password
                        )
        query = db.session.query(User).filter(User.email == request.form.get('email')).first()
        if query:
            error = "Email associated with existing account"
            flash("Email associated with existing account")
            return redirect(url_for('login', error=error))
        db.session.add(new_user)
        db.session.commit()
        #Log in and authenticate user after adding details to database
        login_user(new_user)

        return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":

            email = request.form.get('email')
            password = request.form.get('password')

            #Find user by email entered
            user = db.session.query(User).filter(User.email == email).first()
            if user:
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect(url_for('secrets'))
                else:
                    error = "Invalid credentials"

            else:
                flash("User does not exist")
                error = "User not found"
                return redirect(url_for('login', error=error))

    return render_template("login.html", error=error)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route('/download/<path:filename>')
@login_required
def download(filename):
    # filename = "static/files/cheat_sheet.pdf"
    UPLOAD_FOLDER = "static/files/"
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
