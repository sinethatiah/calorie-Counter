# Calorie Counter
 
A simple Django web app for logging food items and tracking total calories consumed. Built as a school project.
 
## Features
 
- Add food items with their calorie count
- View all logged food in a table
- See a running total of calories
- Reset all entries with one click
- Manage entries through the Django admin panel
## Tech Stack
 
- Python / Django
- Bootstrap 5 (via CDN) for styling
- SQLite (default Django database)
 
## Setup
 
1. Clone or download the project.
2. Create and activate a virtual environment:
```
   python -m venv myenv
   myenv\Scripts\activate      # Windows
   source myenv/bin/activate   # macOS/Linux
```
3. Install Django:
```
   pip install django
```
4. Run migrations:
```
   python manage.py makemigrations
   python manage.py migrate
```
5. (Optional) Create a superuser to access the admin panel:
```
   python manage.py createsuperuser
```
6. Start the development server:
```
   python manage.py runserver
```
7. Visit `http://127.0.0.1:8000/` in your browser.