import json
import psycopg2
import os

def lambda_handler(event, context):
    # Database connection parameters
    db_host = "mcapostgresdb.c3i2koy6e5h5.us-east-1.rds.amazonaws.com"
    db_name = "postgressdb"
    db_user = "test"
    db_password = "test1234"
    db_port = "5432"
    
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port
        )
        
        # Check if the connection is successful
        if connection:
            message = "Connection to PostgreSQL database was successful."
        
        # Close the connection
        connection.close()
        
    except Exception as e:
        message = f"Failed to connect to PostgreSQL database. Error: {str(e)}"
    
    # Return the result
    return {
        "statusCode": 200,
        "body": json.dumps(message)
    }
