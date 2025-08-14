from app.app import create_app

app_ = create_app()

if __name__ == "__main__":
    app_.run(debug=True, host="0.0.0.0", port=5000)
