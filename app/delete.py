from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)
import sqlite3
import os

delete_bp = Blueprint("delete", __name__, template_folder="templates", url_prefix="/delete")
@delete_bp.route("/", methods=["GET", "POST"])
def delete():
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'databases', 'user-data.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    user_id = session.get('userId')
    if user_id == None:
        flash("Your session has expired. Please log in to continue.")
        return redirect(url_for("landing.landing"))
    
    if request.method == "POST":
        day = request.form.get("day-chooser")

        table_name = f"{day.upper()}_{user_id}" if user_id else None

        query = f"""--sql
        SELECT id, starttime, endtime, task FROM {table_name};
        """
        cursor.execute(query)

        records = cursor.fetchall()
        connection.close()
        
        session["records"] = records
        return redirect(url_for("delete.del_view", day=day))
        
    return render_template("delete.html")

@delete_bp.route("/del", methods=["GET", "POST"])
def del_view():
    day = request.args.get("day", "Monday")
    
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'databases', 'user-data.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    if request.method == "POST":
        slot_id = request.form.get("slot-chooser")
        user_id = session.get('userId')
        table_name = f"{day.upper()}_{user_id}" if user_id else None
        
        query = f"""--sql
        DELETE FROM {table_name} WHERE id = ?
        """
        
        cursor.execute(query, (slot_id, ))
        connection.commit()
        connection.close()
        
        flash("Task cleared — making space for what’s next!")
        return redirect(url_for("delete.delete"))
    
    records = session.get("records", [])
    session.pop("records", None)
    return render_template("del.html",  day=day, records=records)
    