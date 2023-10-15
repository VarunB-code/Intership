
# Import the necessary libraries
import re

# Function to convert a dictionary of food items into a string
def get_str_from_food_dict(food_dict: dict):
    # Use a list comprehension to create a list of strings in the format "value key"
    # for each key-value pair in the food_dict dictionary.
    # Then join these strings with commas to create a single string.
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result

# Function to extract the session ID from a session string
def extract_session_id(session_str: str):
    # Use a regular expression to search for the pattern "/sessions/(.*?)/contexts/"
    # in the session_str string.
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    
    # If the pattern was found, extract the matched string and return it.
    if match:
        extracted_string = match.group(0)
        return extracted_string

    # If the pattern was not found, return an empty string.
    return ""