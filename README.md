# Book Review Central

## About

Book Review Central is a web application about books. It includes features such as search, reviews and ratings, data from Goodreads via API, as well as its own API route which produces book data and review statistics in JSON format. Users must be registered and logged in in order to use the app.

It is built with Python using flask - using sqlalchmey for database queries. All database queries are made with pure SQL instead of the ORM so that I could become more comfortable with SQL.

#### Challenges and accomplishments:
 * setting up a development environment for use with Python, flask, and Postgres
 * gained comfort with Python, flask, and Jinja2
 * utilized SQL via Postgres database hosted on Heroku
 * hashing passwords using a library
 * server side input validation
 * UX and UI testing
 

### Dependencies
* Flask
* Flask-Session
* psycopg2
* SQLAlchemy
* Flask-bcrypt
* requests

*also uses Bootstrap 4 and Font Awesome icons.

### What's included:

**`application.py`** - main file for web app.

**`import.py`** - Python script to import CSV file of book data into database

**`/templates/`** - folder containing HTML files
* template.html - template for web app pages
* index.html - registration and log in page
* search.html - search for a book
* books.html - displays a list of search results
* book.html - displays individual book and its reviews

**`/static/`** - folder containing CSS stylesheet
* styles.css - main stylesheet

### API Access

queries can be made to the API via the route `/api/ISBN` where `ISBN` is a valid 10-digit ISBN that is in our database



