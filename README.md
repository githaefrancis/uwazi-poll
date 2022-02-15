To run the application locally, 
1. Clone the project

2. Navigate into the project folder(uwazi-poll)

3. Create your own branch 

eg 
```
git checkout -b feature/admin
```
4. Create a virtual environment
```
python3 -m venv virtual

```
5. activate the virual environment
```
source virtual/bin/activate
```


6. create .env file
It should contain the secret key
eg 
```
export SECRET_KEY=123
```

7. Install the dependencies 

```
pip install -r requirements.txt

```

8. Create a database called uwazi_poll

9. Modify the SQL_ALCHEMY_URI to match your database connection(in DevConfig).

10. grant permission to start.sh file

```
chmod a+x start.sh
```

11. Run the project


```
./start.sh
```

