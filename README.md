## **Rock-Paper-Scissors API Test Challenge**

**Introduction**:
You've been provided with a Rock-Paper-Scissors API. Your task is to write a series of tests against this API to ensure its correctness. Along with the basic tests, you also need to test if the computer's weapon choices are indeed random.

**API Endpoints**:

- `POST /api/play`: 
    - Request payload: 
        ```json
        {
            "choice": "ROCK" | "PAPER" | "SCISSOR"
        }
        ```
    - Response status code: 200
    - Response payload:
        ```json
        {
            "your_weapon": "ROCK" | "PAPER" | "SCISSOR",
            "computer_weapon": "ROCK" | "PAPER" | "SCISSOR",
            "winner": "YOU_WIN" | "DRAW" | "COMPUTER_WINS"
        }
        ```

- `GET /health`:
  - Response status code: 200 
  - Response payload:
    ```json
    {
    "status": "OK"
    }
    ``` 

**Test Requirements**:

1. **Basic Tests**:
    - Test if the API is up and running.
    - Test if the API returns a 400 error for an invalid weapon choice.
    - Test if the API returns a valid response for each valid weapon choice.

2. **Game Logic Tests**:
    - Test if the game logic is correct:
        - When you play ROCK and the computer plays SCISSOR, you should win.
        - When you play ROCK and the computer plays PAPER, the computer should win.
        - When you play ROCK and the computer plays ROCK, it should be a draw.
        - ... and so on for other weapon choices.

3. **Randomness Test**:
    - Run the play endpoint multiple times (e.g., 1000 times) and record the computer's choice each time.
    - Calculate the percentage for each weapon choice (ROCK, PAPER, SCISSOR).
    - Test if the distribution of each weapon choice is approximately equal. (You can use a tolerance level. For instance, if each choice's distribution is within 30%-40%, then it can be considered random.)

**Hints**:

1. For the basic and game logic tests, you might want to use assertions to ensure that the returned values match the expected values.
2. For the randomness test, keep a count of each of the computer's choices and then calculate the distribution percentage.

**Expected Deliverables**:

- A test script containing all the tests.
- A report detailing:
    - The outcome of each test (PASS/FAIL).
    - For the randomness test, a distribution percentage of each weapon choice and an analysis/comment about the randomness based on the results.

**Evaluation Criteria**:

1. **Correctness**: All tests should be correct and meaningful.
2. **Coverage**: Tests should cover all the mentioned scenarios.
3. **Code Quality**: Test scripts should be well-organized, readable, and maintainable.
4. **Analysis**: The randomness test analysis should be well-reasoned.

### Local Setup & Run
1. **Install Dependencies**: Navigate to your project directory and install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the API locally**: Use Uvicorn to run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

### Docker Setup & Run
1. **Build the Docker Image**: Navigate to your project directory (where the `Dockerfile` is located) and build the Docker image:
   ```bash
   docker build -t rock-paper-scissors-api .
   ```

2. **Run the Docker Container**: After building, run the image:
   ```bash
   docker run -p 8080:8080 rock-paper-scissors-api
   ```

### Accessing the API
Once the server is running, the API endpoints can be accessed at `http://localhost:8080`.

### Swagger Documentation
FastAPI provides automatic interactive API documentation with Swagger UI. Once your server is up and running, you can explore and test the API endpoints using Swagger by navigating to:

```
http://localhost:8080/docs
```

This interface allows you to see all available endpoints, their required parameters, request and response models, and even try out the endpoints directly from the web page.
