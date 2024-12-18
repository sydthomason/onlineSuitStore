This application creates a very simple online suit store.

This version is updated to work with Django 5 and Python 3.11 and implements product inventory.

This application was forked from the example store, and updated by Group 4 (Sydney, Derek, Erich, and Amy). 

To use this application:
Start PyCharm and close any projects
Select 'Get From VCS' in the upper right corner of the Pycharm window
Copy-and-paste the URL link to the GitHub repository containing this project's files
Answer Yes when prompted to install requirements
Close the error message displayed after the project is created related to the existing manage.py file. You may ignore
this message.

Close any popup window related to Database Connection Parameters. It is not used.

Open the Terminal Window:
Install the requirements for the project by executing this command in the Terminal window:
pip install -r requirements.txt

Make the migrations for the database model to prepare the data model and create the database:
   python manage.py makemigrations
   python manage.py migrate

Create a superuser with your personal credentials:
   python manage.py createsuperuser

Run the application server by entering the following command in the Terminal window:
python manage.py runserver

Run the server as Admin to add new Collections and Products to the database.
http://127.0.0.1:8000/admin

View the application in your browser and add and remove items to and from the cart. Place an order
http://127.0.0.1:8000

Project Organization:
1. 'myshop' is the main project app
2. 'orders' and 'shop' are apps created as part of this project
3. 'cart' is the shopping cart managed through Django sessions.
4. The 'products' and ''media/products' folders contain product images added to the database

If an Error occurs when installing Pillow:
To use Pillow with Python 3.8.x - upgrade pip to the most recent version (20.x)
easy_install -U pip

Then, install the requirements for the project:
pip install -r requirements.txt

Then create the database:
python manage.py makemigrations
python manage.py migrate
000
