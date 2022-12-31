# Content Finder Backend

The Backend side of the application which is headless and built using Python Django Stack and has the REST API using the Django Rest Framework

### To Use this headless backend

1. Clone you respository or download the zip file

2. create a virtual env and activate it

    - helps you use your django project in a seperate environment

3. go to the root folder -> pip install -r requirements.txt

    - This will install all the dependencies in your new environment

4. Run the below to migrate your database changes

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Finally, `python manage.py runserver` to run the application

6. Create a stripe account and you will have a public key and a secret key. Copy both and paste it in the env files repectively

### FOR THE ENV FILES

-   create a .env file in the settings.py folder
-   add FRONTEND_URL (holds frontend url), BACKEND_URL (holds backend url), STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
