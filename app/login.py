from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    get_flashed_messages
)
import sqlite3
import os

login_bp = Blueprint("login", __name__, template_folder="templates", url_prefix="/login")

@login_bp.route("/", methods=["GET", "POST"])
def login():
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'databases', 'user-data.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        query = """--sql
        SELECT 1 FROM users WHERE username = ? LIMIT 1;
        """
        
        cursor.execute(query, (username,))
        user_exists = cursor.fetchone()
        if not user_exists:
            flash("Username does not exist!")
            return redirect(url_for("login.login"))

        query = """--sql
        SELECT password FROM users WHERE username = ? LIMIT 1;
        """
        
        cursor.execute(query, (username,))
        stored_password = cursor.fetchone()
        
        if not stored_password or stored_password[0] != password:
            flash("Incorrect password!")
            return redirect(url_for("login.login"))
        
        query = """--sql
        SELECT name FROM users WHERE username = ? LIMIT 1;
        """
        
        cursor.execute(query, (username,))
        name = cursor.fetchone()
        session['name'] = name[0] if name else "Guest"
        
        query = """--sql
        SELECT id FROM users WHERE username = ?;
        """
        cursor.execute(query, (username,))
        user_id = cursor.fetchone()
        
        id = user_id[0] if user_id else None
        session['userId'] = id
        
        flash("You’ve successfully signed in!")
        return redirect(url_for("home.home"))
    
    connection.close()

    return render_template("login.html")
