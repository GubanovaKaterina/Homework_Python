from sqlalchemy import create_engine, text, insert

db_connection_string = "postgresql://postgres:321@localhost:5432/postgres"
db = create_engine(db_connection_string)

def create_group_student_table():
    sql = text("""CREATE TABLE group_student (user_id INTEGER, group_id INTEGER)""")
    with db.connect() as connection:
        connection.execute(sql)

def insert_group_student(user_id, group_id):
    sql = text("INSERT INTO group_student (user_id, group_id) VALUES (:user_id, :group_id)")
    with db.connect() as connection:
        connection.execute(sql, {"user_id": user_id, "group_id": group_id})

def update_group_student(user_id, new_group_id):
    sql = text("UPDATE group_student SET group_id = :new_group_id WHERE user_id = :user_id")
    with db.connect() as connection:
        connection.execute(sql, {"new_group_id": new_group_id, "user_id": user_id})

def select_group_student():
    sql = text("SELECT * FROM group_student")
    with db.connect() as connection:
        result = connection.execute(sql)
        rows = result.fetchall()
        return rows

def drop_group_student_table():
    sql = text("DROP TABLE IF EXISTS group_student")
    with db.connect() as connection:
        connection.execute(sql)


def test_group_student_operations():
    create_group_student_table()
    
    insert_group_student(1, 101)
    insert_group_student(2, 102)
    insert_group_student(3, 101)

    update_group_student(1, 103)
    
    rows = select_group_student()
    
    assert len(rows) == 3
    
    drop_group_student_table()