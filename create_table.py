import psycopg2

def create_swear_count_table(db_connect):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_swear_count(
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        swear_count INT NOT NULL,
        detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    print(create_table_query)

    with db_connect.cursor() as cur:
        cur.execute(create_table_query)
        db_connect.commit()

if __name__ == "__main__":
    db_connect = psycopg2.connect(
        user='postgres',
        password='4dlstjs4ak!',  # 보안을 위해 실제 비밀번호 사용 시 주의하세요
        host='localhost',
        port='5432',
        database='postgres',
    )
    
    create_swear_count_table(db_connect)