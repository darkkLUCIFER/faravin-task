## Installation
1. Clone the repository:
   git clone https://github.com/darkkLUCIFER/faravin-task.git

2. Create a virtual environment (recommended):
   python -m virtualenv venv

3. Activate the virtual environment:
   venv\Scripts\activate

4. Install the project dependencies:
   pip install -r requirements.txt

5. Migrate the database:
   python manage.py migrate

6. Create a superuser (admin) account:
   python manage.py createsuperuser

7. Start the development server:
   python manage.py runserver


## Technologies Used
1. Django
2. Drf
3. Jwt
