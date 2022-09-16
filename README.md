# Typless UI for automatic invoice processing

## How-to-use
1. Download/clone the repository. Install all requirements from the "requirements.txt" file.

2. In the "config.py" file insert all neccessery information (SECRET_KEY, TYPLESS_API_KEY, TYPLESS_URL). 
Alternatively, if you use a virtual environment, you can set this information in the venv/bin/source file as:
export SECRET_KEY="your-super-secret-key"
Don't forget to unset the variables at deactivation with:
unset SECRET_KEY

3. Navigate to the base project directory in your command line tool and run the command "python run.py". The app runs
in debug mode by default on port 3000. You can change the mode and port in the "run.py" file.

4. Navigate to http://localhost:3000 and use the interface.


## Interface info
Enter a valid email address and upload a ".pdf" file. 
Click the "Process" button and wait until the request is processed. 
After processing the extracted invoice information will be displayed in a preview field. 
If satisfied with the results you can click "Save" and the data gets saved into the local SQLite db.
If not satisfied, you can reset the form with the reset button.


## Typless account
You can create a Typless account on https://app.typless.com
After registration you can follow the documentation on https://docs.typless.com on how to get your API key,
setup a document and train the model.

Enjoy!