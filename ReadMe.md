HOW TO USE THIS API:
1. EXPORT THE POSTMAN COLLECTION IN THE FILES IF YOU WOULD LIKE TO CHECK
2. CREATE A LOCAL_SETTINGS.PY FILE THAT CONNECTS TO YOUR CHOSEN DATABASE
3. ADD A NEW TRANSACTION WITH THIS URL ('http://127.0.0.1:8000/transactions/')
    - PROVIDING THE FULL BODY OF THE TRANSACTION MODEL:
EX: 
    {
        "payer" : "NAME",
        "points": AMOUNT OF POINTS INTEGER FIELD,
        "timestamp": "yyyy-mm-dd"
    }
4. SPEND POINTS USING THIS URL ('http://127.0.0.1:8000/transactions/{<NUMBER-OF-POINTS-HERE>}/')
5. TO CHECK THE PAYER BALANCES USE THIS URL ('http://127.0.0.1:8000/transactions/balance/')
