import psycopg2

def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS user_swear_count (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            swear_count INT NOT NULL,
            detected_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )
        """,
    )
    conn = None
    try:
        # DB 연결
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="4dlstjs4ak!")
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()



if __name__ == '__main__':
    create_tables()
