# Full Stack API Final Project


## Full Stack Trivia

# Backend - Full Stack Trivia API 

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


# Frontend - Full Stack Trivia API 

### Getting Setup

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend). It is recommended you stand up the backend first, test using Postman or curl, update the endpoints in the frontend, and then the frontend should integrate smoothly.

### Installing Dependencies

1. **Installing Node and NPM**<br>
This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

2. **Installing project dependencies**<br>
This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:
```bash
npm install
```
>_tip_: **npm i** is shorthand for **npm install**

# Required Tasks

### Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```

## API Reference


### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys. 

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "Not found"
}
```
The API will return three error types when requests fail:
- 404: Not found
- 405: Unprocessable Entity 
- 422: Resource Not Found

#### GET/categories
- General:
    - Return the list of available questions categories objects, success value, and total number of available categories.

- Sample: `curl http://127.0.0.1:5000/categories`

``` {"categories":
    {"1":"Science",
    "2":"Art",
    "3":"Geography",
    "4":"History",
    "5":"Entertainment",
    "6":"Sports"},
    "current_category":null,
    "succes":true,
    "total_categories":6}
```

#### GET/questions
- General:
    - Return the list of available categories, questions objects, success value, and total number of questions.
    - Questions results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.

- Sample: `curl http://127.0.0.1:5000/questions`

``` 
{"categories":
{"1":"Science",
"2":"Art",
"3":"Geography",
"4":"History",
"5":"Entertainment",
"6":"Sports"},
"current_category":null,
"questions":[{"answer":"Tom Cruise",
"category":5,"difficulty":4,"id":4,
"question":"What actor did author Anne Rice first denounce, 
then praise in the role of her beloved Lestat?"},
{"answer":"Maya Angelou","category":4,
"difficulty":2,"id":5,"question"
:"Whose autobiography is entitled 
'I Know Why the Caged Bird Sings'?"},
{"answer":"Edward Scissorhands",
"category":5,"difficulty":3,"id":6,
"question":"What was the title of the 1990 fantasy directed by Tim Burton 
about a young man with multi-bladed appendages?"},
{"answer":"Muhammad Ali","category":4,
"difficulty":1,"id":9,"question":
"What boxer's original name is Cassius Clay?"},
{"answer":"Brazil","category":6,"difficulty":3,"id":10,
"question":"Which is the only team to play in every soccer World Cup
 tournament?"},{"answer":"Uruguay","category":6,
 "difficulty":4,"id":11,"question":"Which country 
 won the first ever soccer World Cup in 1930?"},
 {"answer":"George Washington Carver","category":4,
 "difficulty":2,"id":12,"question":"Who invented Peanut Butter?"},
 {"answer":"Lake Victoria","category":3,"difficulty":2,"id":13,
 "question":"What is the largest lake in Africa?"},
 {"answer":"The Palace of Versailles",
 "category":3,"difficulty":3,"id":14,"question":"In which royal 
 palace would you find the Hall of Mirrors?"},{"answer":"Agra",
 "category":3,"difficulty":2,"id":15,"question":"The Taj Mahal is 
 located in which Indian city?"}],"success":true,"total_questions":23}
```

#### DELETE /questions/{question_id}
 - General:
    - Deletes the question of the given ID if it exists. Returns the id of the deleted question, 
    success value and total questions. 
- `curl -X DELETE http://127.0.0.1:5000/questions/5`

```
{"deleted":5,
"success":true,
"total_questions":22}
```

#### POST /questions
- General:
    - Creates a new question using the sumbitted, question, answer, difficulty and category.
    Returns the id of the created question, success value, total questions.
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json"
 -d '{"question":"example question?", "answer":"example answer", "difficulty":3, "category":1}'`

```
{"create":27,
"success":true,
"total_questions":22}
 ```
 
 
#### POST /questions/search
- General:
    - Return a new question based on the string submitted in case insensitive searchTerm parameter.
    - Returns the questions founded, success value, total questions.
    - Questions results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: `curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm":"Author"}'`

```
{"current_category":null,
"questions":[{"answer":
"Tom Cruise",
"category":5,
"difficulty":4,
"id":4,"question":"What actor did author Anne Rice first denounce, 
then praise in the role of her beloved Lestat?"}],
"success":true,"total_questions":1}
 ```
 
 
 
#### GET/categories/{id}/questions
- General:
    - Return the list of available questions based on a category id, success value, 
    current category, questions and number of questions.
    - Questions results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.

- Sample: `curl http://127.0.0.1:5000/questions`

``` 
{"current_category":"Science",
"questions":[{"answer":"The Liver","category":1,
"difficulty":4,"id":20,"question":
"What is the heaviest organ in the human body?"},
{"answer":"Alexander Fleming","category":1,"difficulty":3,
"id":21,"question":"Who discovered penicillin?"},
{"answer":"Blood","category":1,"difficulty":4,"id":22,"question":"
Hematology is a branch of medicine involving the study of what?"}],
"success":true,"total_questions":22}
```

#### POST /quizz
- General:
    - Returns a random question based on a category and not present in the previos question parameter.
    - Returns the id of the created question, success value, total questions.

- Sample: `curl http://127.0.0.1:5000/quizz -X POST -H "Content-Type: application/json" -d '{'previous_questions': [20], 'quiz_category': {'type': 'Science', 'id': '1'}}
'`

```
{"success":true,
"question": {
        'id': 1,
        'question': 'Example',
        'answer': 'Answer', 
        'difficulty': 5,
        'category': 4
    }}
 ```

