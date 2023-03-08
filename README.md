# [Soft UI Dashboard Flask]

Open-source **Flask Dashboard** generated by `Zakaria`

<br />

## ✨ Start the app in Docker

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 
```bash
$ git clone https://github.com/zakita1999/flask-soft-ui.git
$ cd flask-soft-ui
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`
```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## ✨ Manual Build

> 👉 Download the code 
```bash
$ git clone https://github.com/zakita1999/flask-soft-ui.git
$ cd flask-soft-ui
```

<br />

### 👉 Set Up for `Unix`, `MacOS`, `Windows`

> Install modules via `VENV`  
```bash
$ python -m venv myenv  
$ myenv\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Start the app
```bash
$ py app.py
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

### 👉 Create Database Mysql posdb

import the database 'posdb.sql'
    database name : 'posdb'
    username : 'root'
    password : ''
    host : 'localhost'

- Start the app via `flask run`
- Access the `registration` page and create a new user:
  - `http://127.0.0.1:5000/register`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:5000/login`

<br />
