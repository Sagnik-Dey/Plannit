from flask import (
    Blueprint,
    render_template,
    url_for,
    request,
    redirect,
    session,
    flash
)
import sqlite3
import os

register_bp = Blueprint('register', __name__, template_folder="templates", url_prefix="/register")

@register_bp.route("/", methods=["GET", "POST"])
def register():
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'databases', 'user-data.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    if request.method == "POST":
        username = request.form.get("username")
        name = request.form.get("name")
        password = request.form.get("password")
        
        query = """--sql
        SELECT username FROM users WHERE username = ?;
        """
        cursor.execute(query, (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register.register"))
        
        query = """--sql
        INSERT INTO users (username, name, password) VALUES (?, ?, ?);
        """

        cursor.execute(query, (username, name, password))
        
        query = """--sql
        SELECT id FROM users WHERE username = ?;
        """
        cursor.execute(query, (username,))
        user_id = cursor.fetchone()
        id = user_id[0] if user_id else None
        
        if id:
            days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            session['userId'] = id
            
            for day in days_list:
                table_name = f"{day.upper()}_{id}"
                
                query = f"""--sql
                    CREATE TABLE IF NOT EXISTS {table_name} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        starttime TEXT NOT NULL,
                        endtime TEXT NOT NULL,
                        task TEXT NOT NULL        
                    );
                """
                
                cursor.execute(query)
                
        connection.commit()
        connection.close()

        session['name'] = name if name else "Guest"
        flash("You’ve successfully signed in!")
        return redirect(url_for("home.home"))       
    
    return render_template("register.html", error=None)