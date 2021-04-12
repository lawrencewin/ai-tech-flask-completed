# Flask Tutorial Endpoint

This is your endpoint for the Flask / PyTorch tutorial. 

## Steps to Run

1. Download [model.th](https://drive.google.com/file/d/1IZU1hjm_etg37_lHilxsH0eae8mmSc0H/view?usp=sharing) from the google drive. Place it in the `/api` folder.
2. From this base directory, `cd api` to go into the api folder and create a Python Virtual Environment with `python3 -m pip venv env`. Activate with `source env/bin/activate` on the terminal.
3. Install pre-requisites: run `python3 -m pip install -r requirements.txt`
4. Set environment variables to run: `export FLASK_APP=app.py && export FLASK_ENV=development`.
5. Run the flask app with `python3 -m flask run`.
6. In a new terminal, navigate to the client folder. From the base repo directory, it's `cd client`. 
7. Install pre-requisites: run `npm install` or `yarn install` depending on which package manager you use.
8. Run the app with `npm start` or `yarn start` depending on your package manager.
9. Have fun classifying dogs and cats!
