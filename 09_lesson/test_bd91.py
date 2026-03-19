import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

db_connection_string = "postgresql://postgres:321@localhost:5432/postgres"
engine = create_engine(db_connection_string)

@pytest.fixture(scope="session")
def setup_database():
    engine = create_engine(db_connection_string)
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS student (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INTEGER,
                group_id INTEGER
            )
        """))
        conn.commit()
    yield
    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS student"))
        conn.commit()

@pytest.fixture(scope="function")
def db_connection():
    connection = engine.connect()
    yield connection
    connection.close()

@pytest.fixture
def cleanup_student(db_connection):
    yield
    db_connection.execute(text("DELETE FROM student WHERE name = 'Тестовый Студент'"))


def test_create_student(db_connection, cleanup_student):
    insert_sql = text("""
        INSERT INTO student (name, age, group_id) 
        VALUES (:name, :age, :group_id)
    """)
    
    db_connection.execute(
        insert_sql, 
        {"name": "Тестовый Студент", "age": 20, "group_id": 1}
    )
    
    select_sql = text("SELECT * FROM student WHERE name = 'Тестовый Студент'")
    result = db_connection.execute(select_sql)
    student = result.fetchone()
    
    assert student is not None
    assert student[1] == "Тестовый Студент"  # name
    assert student[2] == 20                  # age
    assert student[3] == 1                    # group_id
    
    print(f"✅ Студент создан: id={student[0]}, name={student[1]}")

def test_update_student(db_connection):
    insert_sql = text("""
        INSERT INTO student (name, age, group_id) 
        VALUES ('Студент Для Обновления', 22, 2)
    """)
    db_connection.execute(insert_sql)
    
    select_sql = text("SELECT id FROM student WHERE name = 'Студент Для Обновления'")
    result = db_connection.execute(select_sql)
    student_id = result.fetchone()[0]
    
    update_sql = text("""
        UPDATE student 
        SET age = :new_age, group_id = :new_group_id 
        WHERE id = :student_id
    """)
    db_connection.execute(
        update_sql,
        {"new_age": 23, "new_group_id": 3, "student_id": student_id}
    )
    
    check_sql = text(f"SELECT * FROM student WHERE id = {student_id}")
    result = db_connection.execute(check_sql)
    updated_student = result.fetchone()
    
    assert updated_student[2] == 23  
    assert updated_student[3] == 3    
    
    db_connection.execute(text(f"DELETE FROM student WHERE id = {student_id}"))
    
def test_delete_student(db_connection):
    insert_sql = text("""
        INSERT INTO student (name, age, group_id) 
        VALUES ('Студент Для Удаления', 25, 4)
    """)
    db_connection.execute(insert_sql)
    
    select_sql = text("SELECT id FROM student WHERE name = 'Студент Для Удаления'")
    result = db_connection.execute(select_sql)
    student_id = result.fetchone()[0]
    
    check_sql = text(f"SELECT * FROM student WHERE id = {student_id}")
    check_result = db_connection.execute(check_sql)
    assert check_result.fetchone() is not None
    
    delete_sql = text("DELETE FROM student WHERE id = :student_id")
    db_connection.execute(delete_sql, {"student_id": student_id})
    
    final_check = db_connection.execute(check_sql)
    assert final_check.fetchone() is None
    