# django_channels_chat
Real time chat app using Django channels.

## Run w/ Docker

1. Build container

    ```sh
    $ docker-compose up --build -d
    ```
2. Migrate db

    ```sh
    $ docker-compose run web migrate
    ```
3. Create Superuser

    ```sh
    $ docker-compose run web createsuperuser
    Username (leave blank to use 'root'): admin
    Email address:
    Password: secret
    Password (again): secret
    Superuser created successfully.
    ```
4. Go to http://localhost:5000 and login

5. Open a few browser tabs. Try it out!
