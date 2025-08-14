from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    flash
)
from datetime import datetime
import sqlite3
import os

home_bp = Blueprint("home", __name__, template_folder="templates", url_prefix="/home")

def get_today():
    today = datetime.now()
    date_str = today.strftime("%d.%m.%y")
    day_str = today.strftime("%A")
    
    return (date_str, day_str)

@home_bp.route("/")
def home():
    date_data = get_today()
    date_str, day_str = date_data[0], date_data[1]
    
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'databases', 'user-data.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    user_id = session.get('userId')
    table_name = f"{day_str.upper()}_{user_id}" if user_id else None
    
    if user_id == None:
        flash("Your session has expired. Please log in to continue.")
        return redirect(url_for("landing.landing"))
    
    query = f"""--sql
    SELECT starttime, endtime, task FROM {table_name};
    """

    cursor.execute(query)
    records = cursor.fetchall() if table_name else []

    connection.close()
    
    name = session.get('name', 'Guest')
    
    return render_template("home.html", date=date_str, day=day_str, name=name, records=records)