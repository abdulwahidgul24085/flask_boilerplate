## Flask Boilerplate
The idea of the project is provide you a base from where to start your flask project. The structure of the project is based on the Application Package pattern.

Rename the main project and the root file of the application which in this case is flask_bolierplate

## Config
The root of the project has a config file. This contains all the config available locally for the application.

`app.config.from_object(Name_of_the_config_class)`

## Database
The database contains the ORM which is SqlAlchmey based, and migration tool. In the config file we have `SQLALCHEMY_TRACK_MODIFICATIONS` set to `False`. The reason for this that it signal the application everything the database changes. This puts a lot stress on the system.

## Migration
Migration is great tool for version your database. It also help you in moving you database between servers. You would need the following commands to work with flask migrate

`flask db init` This Initates the db in the project.


`flask db migrate -m "first commit"` this creates the migration.


`flask db upgrade` This commits the transation. After this step you can see the changes in your database.


`flask db downgrade` This roles back your latest changes. This is incase if you want to change your database in to the last stable stage.

## Login
THe login section uses the flask-login module. In the route login function. It contains the `next_page` login. This basic coverts 3 scenarios.

..* The user came straight at the login page, and the next variable does not have argument. Then the user will be routed to the index page
..* The user has come in at some other page of the app, and since they aren't logged in or authorized. They have to login first. On successful login they routed to the inital page. The next contains the url without the domain part.
..* The user is in the same state as the pervious explaination. But this time the next_page var has the full url. In this case the users will be routed to the index page.