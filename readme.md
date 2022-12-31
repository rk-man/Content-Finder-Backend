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
