# invesco_application


## Setup and Installation

1. Clone the repository:
    ```
    git clone https://github.com/Mr-Jerry-Haxor/invesco_application.git
    ```

    ```
    cd  invesco_application
    ```

2. Create a Python virtual environment and activate it:
    ```
    python -m venv env
    ```
    
    ```
    source env/bin/activate
    ```
    or

    ```
    "./env/Scripts/activate"
    ```

    

3. Install the project dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```
    python manage.py migrate
    ```

5. Run the server:
    ```
    python manage.py runserver
    ```

Now, you can access the application at `http://localhost:8000`.
