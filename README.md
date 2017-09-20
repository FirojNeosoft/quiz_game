# quiz_game

Steps to run the application

Virtual Environment : Create virtual environment using command virtualenv venv

Activate Environment : Activate the virtual environment using command source venv/bin/activate

Requirements : Install the requirements in virtual environment using command 'pip install -r requirements.txt'

Make Migrations : python manage.py makemigrations

Migrate : Create database using command python manage.py migrate

Create Superuser : Run python manage.py createsuperuser

Load Dummy Data : python manage.py pushinitdata & python manage.py loaddata

Run the Server : Start the server using command python manage.py runserver

Demo accounts

    username- firoj, password- neosoft@123

    username- rushi, password- neosoft@123

    username- sagar, password- neosoft@123

    username- nikhil, password- neosoft@123

    tanant- TCS, api-key - 23cb00a63d7945eba0ff5b846de1b728

    tenant- Accenture, api-key - 3c1a5d88ac914da6a92e860789453779

apis

    Get access token
        url - /api-token-auth/
        method - POST
        params - username, password - Pass these parameters in body eg. {"username" : "firoj", "password" : "neosoft@123"}

    Get questions
        url - /api/questions
        method - GET
        headers - token, api-key - pass these parameters in header section
        params - q (optional)

