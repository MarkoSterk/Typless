# Typless UI for automatic invoice processing

## How-to-use
1. Download/clone the repository. Install all requirements from the "requirements.txt" file. The project is developed with Python 3.9.14.

2. In the "config.py" file insert all neccessery information (SECRET_KEY, TYPLESS_API_KEY, TYPLESS_URL). 
Alternatively, if you use a virtual environment, you can set this information in the venv/bin/source file as:
export SECRET_KEY="your-super-secret-key"
Don't forget to unset the variables at deactivation with:
unset SECRET_KEY

3. Navigate to the base project directory in your command line tool and run the command "python run.py". The app runs
in debug mode by default on port 3000. You can change the mode and port in the "run.py" file.

4. Navigate to http://localhost:3000 and use the interface.


## API endpoints
The API endpoints are:
1. [POST] "/api/v1/data/process"; excepts a POST request with form object which contains a valid
                                    email field and a single .pdf file (invoice). Returns a 200 status code
                                    with the processed data from Typless as JSON

2. [POST] "/api/v1/data/save"; excepts a POST request with JSON payload with the retuned data from the Typless API.
                                Returns a 201 status code (created) along with a JSON response containing the data and additional
                                status related info.

3. [GET] "/api/v1/data/get_all"; GET request which returns ALL saved records in the local SQLite DB. Returns a 200 status code
                                along with JSON data containing the records and some additional info.

4. [GET] "/api/v1/data/get/<int:id>; GET request which returns ONE saved record with the provided ID.
                                    Returns a 200 status code along with JSON data containing the requested record and some additional info.

5. [DELETE] "/api/v1/data/delete/<int:id>; DELETE request which deletes ONE saved record with the provided ID.
                                            Returns a 204 status code (no content).

## Interface info
Enter a valid email address and upload a ".pdf" file. 
Click the "Process" button and wait until the request is processed. 
After processing the extracted invoice information will be displayed in a preview field. 
If satisfied with the results you can click "Save" and the data gets saved into the local SQLite db.
If not satisfied, you can reset the form with the reset button.


## SQLite database
All processed data gets saved into a local SQLite DB. If you download/clone the repo you will get a copy of the DB with some test entries.
If you wish, you can delete the "site.db" file and start a new one. You can do that by deleting the file and uncommenting this section of code
in the __init__.py file in the "app" directory.

```
from app.models.data import Data

with app.app_context():
    db.create_all()
```

Once you re-run the app with "python run.py" a blank "site.db" file will be created. You can than comment the code back out.

## Typless account
You can create a Typless account on https://app.typless.com
After registration you can follow the documentation on https://docs.typless.com on how to get your API key,
setup a document and train the model.

Enjoy!