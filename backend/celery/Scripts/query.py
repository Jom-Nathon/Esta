# from crate import client
import psycopg2
from psycopg2 import sql
import psycopg2.extras

# connection = client.connect("http://localhost:5432/", username="crate")

def create(table):
    #Create table according to the table name
    if table == 'api_plot' :
        try:
            connection = psycopg2.connect(host="localhost", port="5432", user="postgres", password="jommy348")
            cursor = connection.cursor()
            queryCheck = sql.SQL("""
                SELECT EXISTS (
                    SELECT 1 FROM INFORMATION_SCHEMA.TABLES 
                    WHERE TABLE_SCHEMA = 'public' AND TABLE_NAME = 'api_plot'
                )
                """)
            
            cursor.execute(queryCheck)
            exists = cursor.fetchone()[0]  # This will be True if the table exists, False otherwise

            if not exists:
                queryCreate = sql.SQL("""
                    CREATE TABLE api_plot (
                        plot_id UUID ,
                        plot_case_number VARCHAR(255) NOT NULL,
                        plot_lot_number VARCHAR(255) NOT NULL,
                        plot_sale_order VARCHAR(255)  NOT NULL,
                        plot_type VARCHAR(255) NOT NULL,
                        plot_size FLOAT NOT NULL,
                        plot_upload_date VARCHAR(255) NOT NULL,
                        PRIMARY KEY (plot_id),
                        constraint fk_plots_plot_case
                            foreign key (plot_case_number)
                            REFERENCES plot_case (case_number)
                    )""")
                cursor.execute(queryCreate)

        except psycopg2.Error as e:
            print(f"Error creating table: {e}")
        connection.commit()
        connection.close()
        cursor.close()

    elif table == 'plot_picture' :
        try:
            connection = psycopg2.connect(host="localhost", port="5432", user="postgres", password="jommy348")
            cursor = connection.cursor()
            queryCheck = sql.SQL("""
                SELECT EXISTS (
                    SELECT 1 FROM INFORMATION_SCHEMA.TABLES 
                    WHERE TABLE_SCHEMA = 'public' AND TABLE_NAME = 'plot_picture'
                )
                """)
            
            cursor.execute(queryCheck)
            exists = cursor.fetchone()[0]  # This will be True if the table exists, False otherwise

            if not exists:
                queryCreate = sql.SQL("""
                    CREATE TABLE plot_picture (
                        picture_id UUID DEFAULT gen_random_uuid() ,
                        picture_link VARCHAR(255) NOT NULL,
                        picture_plot_id UUID,
                        PRIMARY KEY (picture_id),
                        constraint fk_plot_picture_plots
                            foreign key (picture_plot_id)
                            REFERENCES plots (plot_id)
                    )""")
                cursor.execute(queryCreate)

        except psycopg2.Error as e:
            print(f"Error creating table: {e}")
        connection.commit()
        connection.close()
        cursor.close()

    elif table == 'plot_map' :
        try:
            connection = psycopg2.connect(host="localhost", port="5432", user="postgres", password="jommy348")
            cursor = connection.cursor()
            queryCheck = sql.SQL("""
                SELECT EXISTS (
                    SELECT 1 FROM INFORMATION_SCHEMA.TABLES 
                    WHERE TABLE_SCHEMA = 'public' AND TABLE_NAME = 'plot_map'
                )
                """)
            
            cursor.execute(queryCheck)
            exists = cursor.fetchone()[0]  # This will be True if the table exists, False otherwise

            if not exists:
                queryCreate = sql.SQL("""
                    CREATE TABLE plot_map (
                        map_id UUID DEFAULT gen_random_uuid() ,
                        map_link VARCHAR(255) NOT NULL,
                        map_plot_id UUID,
                        PRIMARY KEY (map_id),
                        constraint fk_plot_map_plots
                            foreign key (map_plot_id)
                            REFERENCES plots (plot_id)
                    )""")
                cursor.execute(queryCreate)

        except psycopg2.Error as e:
            print(f"Error creating table: {e}")
        connection.commit()
        connection.close()
        cursor.close()

    elif table == 'plot_sale' :
        try:
            connection = psycopg2.connect(host="localhost", port="5432", user="postgres", password="jommy348")
            cursor = connection.cursor()
            queryCheck = sql.SQL("""
                SELECT EXISTS (
                    SELECT 1 FROM INFORMATION_SCHEMA.TABLES 
                    WHERE TABLE_SCHEMA = 'public' AND TABLE_NAME = 'plot_sale'
                )
                """)
            
            cursor.execute(queryCheck)
            exists = cursor.fetchone()[0]  # This will be True if the table exists, False otherwise

            if not exists:
                queryCreate = sql.SQL("""
                    CREATE TABLE plot_sale (
                        sale_id UUID DEFAULT gen_random_uuid() ,
                        sale_date VARCHAR(255) NOT NULL,
                        sale_status VARCHAR(255)  NOT NULL,
                        sale_plot_id UUID,
                        PRIMARY KEY (sale_id),
                        constraint fk_plot_sale_plots
                            foreign key (sale_plot_id)
                            REFERENCES plots (plot_id)
                    )""")
                cursor.execute(queryCreate)

        except psycopg2.Error as e:
            print(f"Error creating table: {e}")
        connection.commit()
        connection.close()
        cursor.close()

    elif table == 'plot_price' :
        try:
            connection = psycopg2.connect(host="localhost", port="5432", user="postgres", password="jommy348")
            cursor = connection.cursor()
            queryCheck = sql.SQL("""
                SELECT EXISTS (
                    SELECT 1 FROM INFORMATION_SCHEMA.TABLES 
                    WHERE TABLE_SCHEMA = 'public' AND TABLE_NAME = 'plot_price'
                )
                """)
            
            cursor.execute(queryCheck)
            exists = cursor.fetchone()[0]  # This will be True if the table exists, False otherwise

            if not exists:
                queryCreate = sql.SQL("""
                    CREATE TABLE plot_price (
                        price_plot_id UUID ,
                        price_professional FLOAT,
                        price_enforcer FLOAT NOT NULL,
                        price_legalgov FLOAT,
                        price_committee FLOAT,
                        price_predictive FLOAT,
                        price_real FLOAT,
                        PRIMARY KEY (price_plot_id),
                        constraint fk_plot_price_plots
                            foreign key (price_plot_id)
                            REFERENCES plots (plot_id)
                    )""")
                cursor.execute(queryCreate)

        except psycopg2.Error as e:
            print(f"Error creating table: {e}")
        connection.commit()
        connection.close()
        cursor.close()

    elif table == 'plot_case' :
        try:
            connection = psycopg2.connect(host="localhost", port="5432", user="postgres", password="jommy348")
            cursor = connection.cursor()
            queryCheck = sql.SQL("""
                SELECT EXISTS (
                    SELECT 1 FROM INFORMATION_SCHEMA.TABLES 
                    WHERE TABLE_SCHEMA = 'public' AND TABLE_NAME = 'plot_case'
                )
                """)
            
            cursor.execute(queryCheck)
            exists = cursor.fetchone()[0]  # This will be True if the table exists, False otherwise

            if not exists:
                queryCreate = sql.SQL("""
                    CREATE TABLE plot_case (
                        case_number VARCHAR(255) NOT NULL ,
                        case_province VARCHAR(255) NOT NULL,
                        case_district VARCHAR(255)  NOT NULL,
                        case_sub_district VARCHAR(255) NOT NULL,
                        PRIMARY KEY (case_number)
                    )""")
                cursor.execute(queryCreate)

        except psycopg2.Error as e:
            print(f"Error creating table: {e}")
        connection.commit()
        connection.close()
        cursor.close()

def insert(table, **kwargs):
    # Insert data into table with all arguments
    if table == 'plot_api':
        insert_plots(table, **kwargs)
    # Add other conditions for different tables if necessary


def insert_plots(table, **kwargs):
    psycopg2.extras.register_uuid()
    connection = None
    try:
        connection = psycopg2.connect(host="localhost", port="5432", user="postgres", password="jommy348")
        cursor = connection.cursor()
        
        # Start transaction
        connection.autocommit = False
        
        # Constructing SQL query dynamically based on kwargs
        columns = ', '.join(kwargs.keys())
        values = ', '.join(['%s'] * len(kwargs))
        query = sql.SQL("INSERT INTO {table} ({columns}) VALUES ({values})").format(
            table=sql.Identifier(table),
            columns=sql.SQL(columns),
            values=sql.SQL(values)
        )
        
        # Executing the query with the values from kwargs
        cursor.execute(query, list(kwargs.values()))
        
        # Commit transaction
        connection.commit()
        
    except psycopg2.errors.ForeignKeyViolation as fk_error:
        print(f"Foreign key violation: {fk_error}")
        connection.rollback()  # Rollback transaction on error
    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")
        connection.rollback()  # Rollback transaction on error
    finally:
        if connection:
            connection.close()
            if cursor:
                cursor.close()
    

def drop(table):
    #Drop table
    try:
        connection = psycopg2.connect(host="localhost", port="5432", user="postgres", password="jommy348")
        cursor = connection.cursor()
        query = sql.SQL("DROP TABLE {table}").format(
            table = sql.Identifier(table)
        )
        cursor.execute(query)

    except psycopg2.Error as e:
        print(f"Error deleting table: {e}")
    connection.commit()
    connection.close()
    cursor.close()

def select():
    #Select data from table

    # Select * from information_schema.tables
    # WHERE table_schema='public'

    return NotImplementedError

def selectAll():
    return NotImplementedError

### SPACE FOR TESTING FUNCTION ###


# ***COMMENT FOR SELF***
#Type is basically if plot is with building or not.
# self.lotNumber = lotNumber
# self.saleOrder = saleOrder
# self.ID = ID
# self.type = type
# self.size = size
# self.estimatedPrice = estimatedPrice
# #sub district = tambon
# self.subDistrict = subDistrict
# #district = amphur
# self.district = district
# self.province = province