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

view_bp = Blueprint("view", __name__, template_folder="templates", url_prefix="/view")
@view_bp.route("/", methods=["GET", "POST"])
def view():
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'databases', 'user-data.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    user_id = session.get('userId')
    if user_id == None:
        flash("Your session has expired. Please log in to continue.")
        return redirect(url_for("landing.landing"))
    
    if request.method == "POST":
        day = request.form.get("day-chooser")
        
        if user_id:
            table_name = f"{day.upper()}_{user_id}"
            query = f"""--sql
            SELECT starttime, endtime, task FROM {table_name};
            """
            cursor.execute(query)
            records = cursor.fetchall()
        else:
            records = []
        
        connection.close()
        return render_template("view.html", records=records, day=day)
    
    return render_template("view.html", day=None, records=None)