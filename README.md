# Project Name

## Overview
This project is a web application built using Django that allows users to manage customer records. Users can register, log in, create, update, view, and delete customer records. The application is designed to be simple and user-friendly, providing essential functionalities for managing customer data.

## Features
- **User registration and authentication**
- **Dashboard** to view all customer records
- **Create** new customer records
- **Update** existing customer records
- **View** individual customer records
- **Delete** customer records
- **User logout** functionality

## Technologies Used
- Python
- Django
- HTML/CSS/JS
- SQLite

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/projectname.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd projectname
    ```

3. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

7. **Create a superuser** (optional, for admin access):
    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

9. **Open your web browser** and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage

1. **Register** a new user account.
2. **Log in** with your credentials.
3. Use the dashboard to manage customer records:
    - **Create** a new record
    - **Update** an existing record
    - **View** details of a specific record
    - **Delete** a record
4. **Log out** when finished.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you would like to contribute to this project.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- [Django documentation](https://docs.djangoproject.com/) for guidance on building web applications.
- Any other resources or libraries that were helpful in the development of this project.


