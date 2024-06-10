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
        
        # SQL query to fetch the PostgreSQL version
        version_query = "SELECT version();"
        
        # Execute the version query
        cursor.execute(version_query)
        version = cursor.fetchone()[0]
        
        # SQL query to list all tables in the 'public' schema
        tables_query = """
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public';
        """
        
        # Execute the tables query
        cursor.execute(tables_query)
        tables = cursor.fetchall()
        
        # Extract table names from the result
        table_names = [row[0] for row in tables]
        
        # Close the cursor and connection
        cursor.close()
        connection.close()
        
        # Return the PostgreSQL version and table names as JSON
        return {
            "statusCode": 200,
            "body": json.dumps({
                "version": version,
                "tables": table_names
            })
        }
        
    except Exception as e:
        # Handle any exceptions that occur
        return {
            "statusCode": 500,
            "body": json.dumps(f"Error: {str(e)}")
        }
