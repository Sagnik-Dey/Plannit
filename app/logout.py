from flask import (
    Blueprint,
    url_for,
    redirect,
    session,
    flash
)

logout_bp = Blueprint("logout", __name__, template_folder="templates", url_prefix="/logout")
@logout_bp.route("/")
def logout():
    session.clear()
    
    flash("You’re logged out. Catch you later!")
    return redirect(url_for("landing.landing"))