# Import the necessary libraries
import mysql.connector

# Declare a global variable for the MySQL connection
global cnx

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pandeyji_eatery"
)

# Function to call the MySQL stored procedure and insert an order item
def insert_order_item(food_item, quantity, order_id):
    try:
        # Create a new cursor
        cursor = cnx.cursor()

        # Call the stored procedure to insert an order item
        cursor.callproc('insert_order_item', (food_item, quantity, order_id))

        # Commit the changes to the database
        cnx.commit()

        # Close the cursor
        cursor.close()

        print("Order item inserted successfully!")

        return 1

    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")

        # If an error occurred, rollback the changes
        cnx.rollback()

        return -1

    except Exception as e:
        print(f"An error occurred: {e}")
        
        # If an error occurred, rollback the changes
        cnx.rollback()

        return -1

# Function to insert a record into the order_tracking table
def insert_order_tracking(order_id, status):
    # Create a new cursor
    cursor = cnx.cursor()

    # Insert a record into the order_tracking table
    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))

    # Commit the changes to the database
    cnx.commit()

    # Close the cursor
    cursor.close()

# Function to get the total price of an order
def get_total_order_price(order_id):
    # Create a new cursor
    cursor = cnx.cursor()

    # Execute a SQL query to get the total price of an order
    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)

    # Fetch the result of the query
    result = cursor.fetchone()[0]

    # Close the cursor
    cursor.close()

    return result

# Function to get the next available order ID
def get_next_order_id():
    # Create a new cursor
    cursor = cnx.cursor()

    # Execute a SQL query to get the maximum order ID from the orders table
    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)

    # Fetch the result of the query
    result = cursor.fetchone()[0]

    # Close the cursor
    cursor.close()

    # If no order IDs exist yet, return 1 as the next available order ID,
    # otherwise return one more than the maximum order ID found.
    if result is None:
        return 1
    else:
        return result + 1

# Function to fetch the status of an order from the order_tracking table
def get_order_status(order_id):
    # Create a new cursor
    cursor = cnx.cursor()

    # Execute a SQL query to fetch the status of an order from the order_tracking table
    query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
    
    cursor.execute(query)

    # Fetch the result of the query
    result = cursor.fetchone()

     # Close the cursor
    cursor.close()

     # If a status was found for this order ID, return it,
     # otherwise return None.
    if result:
         return result[0]
    else:
         return None


if __name__ == "__main__":
     print(get_next_order_id())
