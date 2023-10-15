from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import random
import ssl
import uvicorn

# Create a new FastAPI instance
app = FastAPI()

# Define a POST endpoint at the root ("/")
@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']

    # Define a dictionary to map intents to their respective handler functions
    intent_handler_dict = {
        'course.price': handle_course_price,
        'eligibility.age': handle_eligibiliy_age,
        'eligibility.background': handle_eligibility_background
    }

    # Call the appropriate handler function based on the intent and return its result
    return intent_handler_dictintent

# Define a function to handle the 'course.price' intent
def handle_course_price(parameters: dict):
    # Extract the course name and country from the parameters
    course_name = parameters["course-name"]
    country = parameters["geo-country"]

    # Define a dictionary to map course names to their prices
    price_dict = {
        "SQL": 900,
        "Power BI": 2400,
        "Python": 800,
        "Excel": 700,
        "Data Analytics Bootcamp": 4800
    }

    # Get the price of the requested course from the dictionary
    course_price = price_dict.get(course_name)

    # Construct a response containing the course price
    response = {
        "fulfillmentText": f"The course price for {course_name} is : {course_price}"
    }

    # Return a JSON response with the constructed response
    return JSONResponse(content=response)

# Define a function to handle the 'eligibility.age' intent
def handle_eligibiliy_age(parameters: dict):
    # Extract the course name and age from the parameters
    course_name = parameters["course-name"]
    age = parameters["age"]["amount"]

    # Check if the age is greater than 30 and construct an appropriate response
    if age>30:
        answer = random.choice([
            '''There are many folks who have learned necessary data analyst skills at a later age
            and successfully transitioned into a data analyst role. I know one person who made this transition
            at the age of 51 and his past background was physical therapist. I've a video on my YouTube channel 
            that has few such stories highlighted, please watch that to get 
            some tips: https://www.youtube.com/watch?v=nkvInnpuic8 
            In short: we believe it is possible to learn data analytics at this age 
            ''',
            '''
            Hey, It is a common perception that at a later age it is hard to learn new things and switch your career 
            but to be honest I personally know many folks who learned data analytics, data science at 40+ age and made 
            this transition. One other person I know was a physical therapist till age 51 and now he is a data 
            analyst working in a healthcare company. Watch this video to know about few such 
            stories: https://www.youtube.com/watch?v=nkvInnpuic8
            In short, it is 100% possible, if you have an eagerness to learn and a commitment 
            towards making this career switch. 
            Also one great thing about data analyst career is it requires very less coding so it will not 
            be very difficult for you! So yes, you can learn data analysis at your age.
            '''
        ])

    else:
        answer ="Your age is less than 30 and you are too young to learn anything. Just do it my friend."

    if course_name:
        answer += " And yes you are eligible for " + "".join(course_name)

    # Return a JSON response with the constructed response
    return JSONResponse(content={
        "fulfillmentText": answer
    })

# Define a function to handle the 'eligibility.background' intent
def handle_eligibility_background(parameters: dict):
    # Extract the course name and background from the parameters
    course_name = parameters["course-name"]
    background = parameters["degree-or-situation"]

    if background:
        if background == "Mechanical Engineer":
            answer = '''I know many Mechanical Engineers who have successfully become data analysts. Watch these videos 
            for these success stories: (1) https://www.youtube.com/watch?v=4BLxapDqrlA (2) https://www.youtube.com/watch?v=yKB6EUbGamo
            Transition from mechanical engineering to data analyst is definitely possible. You need to learn necessary skills
            such as Excel, Power BI, SQL etc.  
            '''
        elif background == "B.COM":
            answer = '''There are many B.COM graduates who have transitioned into data analytics industry.'''
