# Varun's Internship Project Phase 1

Hello, I'm Varun, a Computer Science Engineering student. This is the first phase of my internship project where I've developed a web application using FastAPI and MySQL. The application is a restaurant ordering system with an integrated chatbot.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project is organized into the following directories:

- `backend`: Contains the backend code for the application, written in Python using the FastAPI framework.
- `db`: Contains a dump of the database. You will need to import this into your MySQL database using a tool like MySQL Workbench.
- `dialogflow_assets`: Contains assets for Dialogflow, such as training phrases for our intents.
- `frontend`: Contains the code for the website.

## Installation

1. Clone the repository to your local machine.
2. Install the necessary dependencies:
    ```
    pip install -r backend/requirements.txt
    ```

## Usage

To start the FastAPI backend server:

1. Navigate to the `backend` directory in your command prompt.
2. Run the following command: `uvicorn main:app --reload`

To set up ngrok for HTTPS tunneling:

1. Visit [https://ngrok.com/download](https://ngrok.com/download) and download the version of ngrok that is suitable for your operating system.
2. Extract the downloaded zip file and place `ngrok.exe` in a folder.
3. Open a command prompt, navigate to that folder, and run this command: `ngrok http 80000`

Please note that ngrok sessions can timeout. If you see a message indicating that the session has expired, you will need to restart the session.

The application provides a user-friendly interface for customers to place their orders and track them in real-time. It also includes a chatbot for customer support.

Here's a brief overview of the project structure:

- `main.py`: This is the main script where the FastAPI application is created and routes are defined.
- `db_helper.py`: This script contains helper functions for database operations.
- `generic_helper.py`: This script contains generic helper functions used across the project.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT