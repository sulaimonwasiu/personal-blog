from flask import Blueprint, render_template, request, redirect, url_for, session, flash

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':  # Simple check
            session['username'] = username
            return redirect(url_for('blog.dashboard'))
        flash("Only the admin is allowed to login.")
    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('blog.index'))