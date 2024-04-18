# FC Manager Rest API
Api service for management Football Clubs written on Flask Rest Api. It has functionality managing teams and players.

Features:
- JWT authentication.
- Documentation via /swagger-ui/
- Implementing 4 models with many-to-many and many-to-one relationships.
- Creating and updating teams and players of the club

## Installing using GitHub
- Fork the project into your GitHub
- Clone it into your dektop
```
git clone https://github.com/jacesca/FlaskFCManagerAPI.git
```
- Setup environment (it requires python3)
```
python -m venv venv
source venv/bin/activate  # for Unix-based system
venv\Scripts\activate  # for Windows
```
- Install requirements
```
pip install -r requirements.txt
```
- Open .env.sample and change environment variables on yours! Rename the file from .env.sample to .env


## Run API Service
```
flask migrate
flask run
```

## Getting Access instructions
- Create a user via **/register/** endpoint
- Get access token via **/login/** endpoint
- Get documentation of the available API endpoints in: http://127.0.0.1:5000/swagger-ui
- Install [ModHeader](https://chromewebstore.google.com/detail/modheader-modify-http-hea/idgpnmonknjnojddfkpgkljpfnnfcklj?pli=1) browser extension and create a Request Header with the name **Authoriazation** and the value **Bearer `<your access token>`
