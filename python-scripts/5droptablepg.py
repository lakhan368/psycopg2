import psycopg2

def delete_table():
    # Database connection parameters
    
    
    
    

  

    # Connection to PostgreSQL
    connection = psycopg2.connect(
        user = 'test',
        password = 'test1234',
        host = 'mcapostgresdb.chaiuouywg8z.us-east-1.rds.amazonaws.com',
        database = 'postgressdb',
        port=5432
    )

    cursor = connection.cursor()

    # SQL query to drop (delete) a table
    drop_table_query = "DROP TABLE IF EXISTS employees;"

    try:
        # Execute the SQL query
        cursor.execute(drop_table_query)
        
        # Commit the transaction
        connection.commit()
        
        print("Table deleted successfully.")

    except Exception as e:
        # Rollback the transaction in case of an error
        connection.rollback()
        
        print("Error:", e)

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()

# Call the function to delete the table
delete_table()
