<h1>User, Client, and Artist Project</h1>
This is a Django project that implements a backend structure for managing users, clients, and artists.
</br>
<h2>Installation</h2>
Clone the repository using the command git clone https://github.com/username/project.git.
</br>Navigate to the project directory using the command cd project.
</br>Run the database migrations using the command python manage.py migrate.

<h2>Usage</h2>
To use the application, start the development server using the command python manage.py runserver and navigate to http://localhost:8000/ in your web browser.
The following REST API endpoints are available:

/api/works - Displays a list of works.
/api/works?artist=[Artist Name] - Filters the list of works by artist.
/api/works?work_type=[Work Type] - Filters the list of works by work type.
/api/register - Registers a new user with a username and password.
