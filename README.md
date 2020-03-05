# image-processing
Final Project of Digital Image Processing Course 

## Features
1. Grayscaling
2. View Histogram
3. Zoom In & Zoom Out
4. Flip Vertical & Flip Horizontal
5. Rotate
6. Crop
7. Cut & Paste

## Installation
1. Create virtual environment for Python 3.6 and activate.
    ```
    $ virtualenv -p python3.6 env
    $ source env/bin/activate
    ```

2. Install requirements.
    ```
    $ pip install -r requirements.txt
    ```

3. Initial migration for django-models.
    ```
    $ python manage.py migrate
    ```

4. Create superuser account.
    ```
    $ python manage.py createsuperuser
    ```
5. Run django web server locally and access `http://localhost:<port>` from browser.
    ```
    $ python manage.py runserver
    ```
