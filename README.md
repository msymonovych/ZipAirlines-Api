# ZipAirlines-Api

## Installation and Setup

Python3 must be already installed

1. Clone the repository:
    ```shell
    git clone https://github.com/msymonovych/ZipAirlines-Api.git
    cd ZipAirlines-Api
    ```
2. Set up virtualenv and activate it:
    #### Linux/Mac:
    ```shell
   python3 -m venv .venv
   source .venv/bin/activate
    ```
   #### Windows:
    ```shell
    python -m venv .venv
    .venv\Scripts\activate
    ```
   
3. Install dependencies:
    ```shell
   pip install -r requirements.txt
    ```
4. Set up database and run migrations:
    ```shell
   pythom manage.py migrate
    ```
5. Run Debug server:

   ```shell
   python mangae.py runserver
   ```
You can now access API by `http://127.0.0.1:8000/` address