from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    flash
)

landing_bp = Blueprint("landing", __name__, template_folder="templates", url_prefix="/")

@landing_bp.route("/")
def landing():
    userId = session.get("userId") 
    
    if userId:
        flash("You’re already signed in. Log out to access a different account.")
        return redirect(url_for("home.home"))
    
    return render_template("landing.html")