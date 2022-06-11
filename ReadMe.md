LAUNCHING YOUR VIRTUAL ENVIRONMENT 
1. In the terminal complete the following steps: 
    - type 'pipenv install'
    - type 'pipenv --venv and copy the path into your python interpreter
    - type 'python manage.py runserver to start the application

HOW TO USE THIS API:
RUNNING THE APPLICATION:
1. Export the postman collection provided in the files
2. Create a local_settings.py file that connects to MySQL database
3. Add a new transaction with the url  ('http://127.0.0.1:8000/transactions/')
    - Providing the full body of the transaction model:
      EX: 
    {
        "payer" : "NAME",
        "points": AMOUNT OF POINTS INTEGER FIELD,
        "timestamp": "yyyy-mm-dd"
    }
4. Spend points inserting the amount of points using this url  ('http://127.0.0.1:8000/transactions/{<NUMBER-OF-POINTS-HERE>}/')
5. To check the payer balances use this url ('http://127.0.0.1:8000/transactions/balance/')