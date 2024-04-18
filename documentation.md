# Starting instructions

## Install Flask in the prepared python environment
```
pip install flask
pip install flask-sqlalchemy
pip install Flask-Migrate
```
To bring API functionalities
```
pip install flask-smorest
pip install marshmallow
```
For API security
```
pip install Flask-JWT-Extended
pip install passlib
```
For Coding Style:
- Black: it is a library that automatically correct the code according to certain rules.
    - To rum it: find the directory and in command line write:
    - black . 
    - black _file-name_.py
- flake8: to identify style caveats there are.
    - To rum it: find the directory and in command line write:
    - flake8 .
    - flake8 _module-folder-name_
```
pip install black
pip install flake8
```

## Verify the flask version
```
flask --version
```

## To run the application
```
flask run
```

## Create the requirement files:
```
conda list -e > requirements.txt
```
or
```
pip freeze > requirements.txt
```
also
```
conda env export > flask_env.yml
```

## To handle migrations
1. Initialize
```
flask db init
```
2. Make the changes to the database
3. Generate the migration version and document it
```
flask --app main db migrate -m "describe the migration" 
```
4. Apply changes to the database
```
flask --app main db upgrade
```

## CRUD Operations
### C: creating & R: reading
```
$ python

from app import app
from models.team import TeamModel

app_ctx = app.app_context()
app_ctx.push()

# Reading
TeamModel.query.all()

# Adding method 1
db.session.add(TeamModel(title="title-1", ...))

# Adding method 2
record2 = TeamModel(title="title-1", ...)
db.session.add(record2)

# to save the changes
db.session.commit()

# More readings
TeamModel.query.all()[1]
# As this item did not exist, gives an Index error
TeamModel.query.all()[5]  # IndexError
TeamModel.query.all()[0].title
TeamModel.query.first()

all_records = TeamModel.query.all()
all_records[0]
TeamModel.query.filter_by(title="title-1").all()
TeamModel.query.get(1)  # Deprecated
db.session.get(TeamModel, 1)
db.session.get(TeamModel, 5)  # Empty result

app_ctx.pop()
exit() <br>
```

### D: deleting
```
$ python

from app import app
from models.team import TeamModel

app_ctx = app.app_context()
app_ctx.push()

record_to_delete = db.session.get(TeamModel, 2) 
db.session.delete(record_to_delete)
db.session.commit()

app_ctx.pop()
exit()
```

### U: updating
```
python

from app import app
from models.team import TeamModel

app_ctx = app.app_context()
app_ctx.push()

record = db.session.get(TeamModel, 1) 
record.title<<fzdf>>
record.title = 'title-1' 
db.session.commit()

app_ctx.pop()
exit()
```

## URLs
- [Current Application](http://127.0.0.1:5000/)
- [Api documentation](http://127.0.0.1:5000/swagger-ui)

## Other documentation
- [Secure Key Generator](https://djecrety.ir/)
- [SQLite Studio](https://sqlitestudio.pl/)
- [flask-smorest](https://flask-smorest.readthedocs.io/en/latest/quickstart.html)
- [Original project code](https://github.com/Codefinity-py/fc_manager_api/blob/develop/schemas.py)
- [Insomnia tool](https://insomnia.rest/) for Design, debug, and test APIs locally or in the cloud
- [HTTP Requests and Responses Explained](https://codefinity.com/blog/HTTP-Requests-and-Responses-Explained)
- [OpenAPI Swagger: CDN for open source projects](https://www.jsdelivr.com/)
- [To handled token in Swagger Documentation: ModHeader](https://chromewebstore.google.com/detail/modheader-modify-http-hea/idgpnmonknjnojddfkpgkljpfnnfcklj?pli=1)
> After adding the extension, follow the next steps: <br>
> 1. Click on chrome extension, look for modheader <br>
> 2. Click on +Mod and add "Authorization" with "Bearer {{access_token}}" replace the {{access_token}} with the proper value <br>
>
> Now you can use the OpenAPI Swagger with the restricted APIs (authorization required). <br>
> Please remove the access token from ModHeader at the end, or you won't be able to navigate other sites in the same browser window.
