import mysql.connector
from generate_spatial_location import generate_spatial_location
import mysql_config

db_name = "geo_db"

if __name__ == "__main__":
    try:
        conn = mysql.connector.connect(**mysql_config.config)
        cur = conn.cursor()

        print("Successfully connected to the database")

        # Create data for inserting
        generated_coordinates = generate_spatial_location(int(1e6))
        prepared_coordinates = ",\n".join(
            [
                generated_coordinates[i].get_point_format()
                for i in range(len(generated_coordinates))
            ]
        )

        # Insert into db
        count = cur.execute(
            f"INSERT INTO GeoLocation (name, position) VALUES {prepared_coordinates};"
        )
        conn.commit()

        print(f"Succesfully add to db table. Row count: {cur.rowcount}")
        cur.close()
    except mysql.connector.Error as Error:
        print("Fail to insert into database. Error :\n", Error)
    finally:
        if conn:
            conn.close()
        print("Connection is closed")
