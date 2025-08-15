# Plannit

<img width="128" height="127" alt="plannit-logo (1)" src="https://github.com/user-attachments/assets/2b072cb1-062e-46ce-8d65-6c3247510113" />

A simple yet effective web-based weekly planner application designed to help users organize their tasks and manage their schedule for the entire week. This application provides a clean, intuitive interface for adding, viewing, and deleting tasks, ensuring you stay on top of your daily responsibilities.

---
<img width="1366" height="636" alt="image" src="https://github.com/user-attachments/assets/98752e17-7b19-4b1e-8511-02c2ee61f44f" />

---

## ✨ Features

* **Secure User Authentication:** Users can securely create a personal account and log in.
* **Dynamic Daily View:** The homepage automatically displays the current date and fetches the schedule specifically for that day, giving you an at-a-glance view of your most urgent tasks.
* **Update and Manage Schedules:** A dedicated "Update" page allows users to add new time slots and tasks for any day of the week, with an easy-to-use form to specify the time range and task description.
* **Comprehensive Weekly View:** The "View" page provides the flexibility to browse your complete schedule for any selected day of the week.
* **Effortless Task Deletion:** Users can easily delete individual tasks or time slots from their schedule on the "Delete" page, helping to keep their planner tidy and up-to-date.
* **Secure Logout:** A prominent logout option is available to securely end the user's session.

---

## 🛠️ Tech Stack

This project is built using a classic combination of backend and frontend technologies.

* **Backend:**
    * **Python:** The core logic of the application is written in Python.
    * **[Flask](https://flask.palletsprojects.com/):** A lightweight and flexible web framework used for handling routing, requests, and managing application logic.

* **Frontend:**
    * **HTML5:** Provides the structure and content for all web pages.
    * **CSS3:** Styles the application.
    * **JavaScript:** Adds interactivity and dynamic behavior to the pages.

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following software installed on your system:

* **Python 3.x**
* **pip** (Python package installer)

### Installation

1.  **Clone the repository:**

2.  **Create and activate a virtual environment:**
    It's recommended to use a virtual environment to manage project dependencies.

    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies:**
    Install all required Python packages from the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

4.  ### Environment Variables

    This project uses environment variables for sensitive settings.

    Create a `.env` file in the project root with the following contents:
    SECRET_KEY=your_random_secret_key_here

    - `SECRET_KEY` → Used by Flask for securely signing the session cookies.  
    **Generate a random one** with:
    ```bash
    python -c "import secrets; print(secrets.token_hex(16))"
    ```
    Add the key to .env file as a value of *SECRET_KEY*

4.  **Run the application:**
    Start the Flask development server.

    ```bash
    flask run
    ```
    The application will now be running at `http://127.0.0.1:5000`.

### If you want to setup using 'uv'
1.  Clone the repository
2.  Sync the requirements: 
    ```bash
    uv sync 
    ```
3.  Run the project
    ```bash
    uv run main.py
    ```

---

## 👨‍💻 Usage

* **Registration:** Navigate to the login page and click the "Create an account" link. Fill out the form to register your new account.
* **Log In:** Use the credentials from your new account to log in.
* **Home:** Upon logging in, you'll be taken to the homepage, which serves as your daily dashboard.
* **Update:** Go to the "Update" page to add a new task for a specific day and time.
* **View:** The "View" page allows you to select any day of the week to see your planned schedule.
* **Delete:** On the "Delete" page, you can choose a task and remove it from your schedule.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
