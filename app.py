import os
from flask import Flask, render_template, redirect, request, session, url_for
 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'strangerthings'

imageFolder = os.path.join('static', 'image')

app.config['UPLOAD_FOLDER'] = imageFolder

@app.route("/")
def index():
    business = os.path.join(app.config['UPLOAD_FOLDER'], 'back.jpg')
    return render_template("index.html", user_image = business)


# users = []
# users.append(User(id=1, username='Christopher', password='password'))
# users.append(User(id=2, username='Lawson', password='secret'))

# @app.before_request
# def before_request():
#     if 'user_id' in session:
#         user = [x for x in users if x.id == session['user_id']][0]

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))
        
        return redirect(url_for('login'))
    
    return render_template('login.html')

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return 'You are now logged out!'

# @app.route('/home')
# @login_required
# def home():
#     return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)