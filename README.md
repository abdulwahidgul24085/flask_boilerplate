## Flask Boilerplate
The idea of the project is provide you a base from where to start your flask project. The structure of the project is based on the Application Package pattern.

Rename the main project and the root file of the application which in this case is flask_bolierplate

## Config
The root of the project has a config file. This contains all the config available locally for the application.

`app.config.from_object(Name_of_the_config_class)`

## Database
The database contains the ORM which is SqlAlchmey based, and migration tool. In the config file we have `SQLALCHEMY_TRACK_MODIFICATIONS` set to `False`. The reason for this that it signal the application everything the database changes. This puts a lot stress on the system.

### Migration
Migration is great tool for version your database. It also help you in moving you database between servers. You would need the following commands to work with flask migrate

`flask db init` This Initates the db in the project.

`flask db migrate -m "first commit"` this creates the migration.

`flask db upgrade` This commits the transation. After this step you can see the changes in your database.

`flask db downgrade` This roles back your latest changes. This is incase if you want to change your database in to the last stable stage.
