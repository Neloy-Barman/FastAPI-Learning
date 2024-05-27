# FastAPI


## Running the app
<ul>
    <li>uvicorn main:app</br>main refers to the fact we are calling the file main.py.
    app means calling the instantiated app.</li>
    <li>If we did hello.py and world = FastAPI(), then it would be uvicorn hello:world.</li>
    <li>uvicorn main:app --port=#PORT</br>We can define port number according to us.</li>
    <li>uvicorn main:app --reload</br>This means we don't need to rerun everytime something is changed.</li>
</ul>


## Swagger documentation
http://127.0.0.1:8000/docs or http://localhost:8000/docs will give us documentation like postman where we can check and test our api.
 




