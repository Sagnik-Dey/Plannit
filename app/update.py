from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)
import sqlite3
import os

update_bp = Blueprint("update", __name__, template_folder="templates", url_prefix="/update")
@update_bp.route("/", methods=["GET", "POST"])
def update():
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'databases', 'user-data.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    user_id = session.get('userId')
    if user_id == None:
        flash("Your session has expired. Please log in to continue.")
        return redirect(url_for("landing.landing"))
    
    if request.method == "POST":
        day = request.form.get("day-chooser")
        start_time = request.form.get("start-time-inp")
        end_time = request.form.get("end-time-inp")
        task = request.form.get("task-inp")

        table_name = f"{day.upper()}_{user_id}"
        query = f"""--sql
        INSERT INTO {table_name} (starttime, endtime, task) VALUES (?, ?, ?);
        """
        cursor.execute(query, (start_time, end_time, task))

        connection.commit()
        connection.close()
        
        flash("Task added! What’s next on your list?")
        return redirect(url_for("update.update"))
    
    connection.close()
    return render_template("update.html")