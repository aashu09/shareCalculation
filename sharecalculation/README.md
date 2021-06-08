# Distribute Share Percentage
A django REST API app to calculating share distribution.


## To Run the project and access the API

Go into project directory, and run below commands on terminal - 

Create a virtual environment for python3 using:

```python3 -m venv environment_name```

Activating a virtual environment:

```source environment_name/bin/activate```

### Run the below commands to set up:
Installing all libraries in requirements file inside the virtual environment:

```pip3 install -r requirements.txt```

Running the project on the localhost:

```python3 manage.py runserver```

Check for running server:

http://localhost:8000/
OR
http://127.0.0.1:8000/

The server is running now. Head on to the below API endpoints:

## CRUD APIs for Category

### Create

```/distribute/```

params:
```json
{
    "total_amount": "100",
    "id1": "user01",
    "share1": "0.02",
    "id2": "user02",
    "share2": "0.04",
    "id3": "user03",
    "share3": "0.15"
}
```

Response:
```json
{
    "status_code": 200,
    "message": "Data Calculated",
    "total_amount": "100",
    "Shares": {
        "user01": "2.0",
        "user02": "4.0",
        "user03": "15.0"
    }
}
```
## Testing

Test using:

````python3 manage.py test````
