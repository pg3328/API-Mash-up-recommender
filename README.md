# Nearest API Finder

This application is designed to provide information about the nearest possible APIs hosted on ProgrammableWeb based on user input. It is built using the Flask framework, which connects the front-end and back-end components. User input is collected through the user interface and passed to the back-end for processing.

## Libraries Used

1. Flask: The Flask framework is utilized to handle the connection between the front-end and back-end components.
2. pymongo: This library is used to communicate with MongoDB and retrieve the necessary information.

## Program Flow

1. Data Collection: The application collects data from a CSV file.
2. Data Parsing and Loading: The collected data is parsed and loaded into MongoDB in advance.
3. MongoDB Integration: The pymongo library is employed to interact with the MongoDB database.
4. User Input: The application prompts the user to provide their API requirements.
5. Requirement Analysis: The user's input is analyzed to determine the relevant query for retrieval.
6. Query Execution: A specific function call is made based on the query requirements determined through analysis.
7. Response Processing: The response from the query is stored as a list and sent to an HTML page to display the results.

## Installation and Usage

To run this application locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Ensure you have a MongoDB instance running locally or provide the necessary connection details in the application code.
4. Run the Flask application by executing `backend.py`.
5. Open your web browser and navigate to `http://localhost:5000`.
6. Input your desired API information in the provided fields and submit the form.
7. The application will retrieve and display the nearest APIs based on your requirements.
