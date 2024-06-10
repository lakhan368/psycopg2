import json
import psycopg2

def lambda_handler(event, context):
    # Database connection parameters
    db_host = "mcapostgresdb.c3i2koy6e5h5.us-east-1.rds.amazonaws.com"
    db_name = "postgressdb"
    db_user = "test"
    db_password = "test1234"
    db_port = "5432"
    
    try:
        # Establish connection to PostgreSQL database
        connection = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port
        )
        
        cursor = connection.cursor()
        
        # SQL query to be executed
        query = "SELECT * FROM your_table_name LIMIT 10;"  # Replace 'your_table_name' with your actual table name
        
        # Execute the query
        cursor.execute(query)
        
        # Fetch all results
        results = cursor.fetchall()
        
        # Convert the results to a list of dictionaries for easier JSON serialization
        columns = [desc[0] for desc in cursor.description]
        data = [dict(zip(columns, row)) for row in results]
        
        # Close the cursor and connection
        cursor.close()
        connection.close()
        
        # Return the results as JSON
        return {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        
    except Exception as e:
        # Handle any exceptions that occur
        return {
            "statusCode": 500,
            "body": json.dumps(f"Error: {str(e)}")
        }
