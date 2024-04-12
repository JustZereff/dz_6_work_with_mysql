import datetime
from random import randint
from connection import create_connection, database


from faker import Faker

Faker.seed(1150)
fake_data = Faker(locale="uk-UA")
fake = Faker()

COUNTER = 5


# print(fake_data.name())
def insert_data(connection, sql_query, data):
    cursor = connection.cursor()
    
    # cursor.executemany(sql_query, [(fake_data.name().split(" "))[:2] for _ in range(COUNTER)])
    cursor.executemany(sql_query, data)
    connection.commit()


if __name__ == "__main__":
    #   Цим запитом з деякими корегуваннями я заповнював таблиці Студентів та Вчителів
    # sql_query = """
    # INSERT OR IGNORE INTO items(first_name, last_name)
    # VALUES (?, ?)
    # """
    # with create_connection(database) as conn:
    #     insert_data(conn, sql_query)
    # print([(fake_data.name().split(" ")) for _ in range(COUNTER)])
    
    # --------------------------------------------------------------------------------------------------
    
    #   Цім запитом я заповнював таблицю предметів та вчителів
    # with create_connection(database) as conn:
    #     # Дістаємо данні з таблиці teachers
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT id, first_name, last_name FROM teachers")
    #     teachers_data = cursor.fetchall()
        
    #     # Створюємо список з предметами
    #     item_list = ["Исторія", "Математика", "Література", "Фізика", "Хімія"]
        
    #     # Генеруємо данні для таблиці items
    #     items_data = []
    #     for i, teacher in enumerate(teachers_data):
    #         teachers_id, first_name, last_name = teacher
    #         item = (item_list[i], teachers_id, first_name, last_name)
    #         items_data.append(item)
    #     print(items_data)
        
    #     # Оновлюємо данні в таблиці items
    #     sql_query_items = """
    #     INSERT INTO items(item, teachers_id, first_name, last_name)
    #     VALUES (?, ?, ?, ?)
    #     """
        
    #     with create_connection(database) as conn:
    #         insert_data(conn, sql_query_items, items_data)

    # --------------------------------------------------------------------------------------------------
    
    #    Генеруємо оцінки студентам
    # with create_connection(database) as conn:
    #     # Дістаємо данні з таблиці students
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT id, first_name, last_name FROM students")
    #     students_data = cursor.fetchall()
    #     # print(len(students_data))
        
    #     # Створюємо список з предметами
    #     item_list = ["Исторія", "Математика", "Література", "Фізика", "Хімія"]
        
    #     # Генеруємо оцінки студентам
        
    #     def generate_grades():
    #         students_evolution = []
    #         for _ in range(len(students_data)):
    #             grades = ','.join(str(randint(1,5)) for _ in range(len(item_list)))
    #             students_evolution.append(grades)
    #         return students_evolution
        
    #     h_grade = generate_grades()
    #     m_grade = generate_grades()
    #     l_grade = generate_grades()
    #     p_grade = generate_grades()
    #     c_grade = generate_grades()
        
    #     # Генеруємо данні для таблиці evaluations
    #     items_data = []
        
    #     for i, student in enumerate(students_data):
    #         student_id, first_name, last_name = student
    #         random_date = fake.date()
    #         item = (random_date, h_grade[i], m_grade[i], l_grade[i], p_grade[i], c_grade[i], student_id, first_name, last_name)
    #         items_data.append(item)
    #     # print(items_data)
        
    #     # Оновлюємо данні в таблиці items
    #     sql_query_items = """
    #     INSERT INTO evaluations(date_received, history_grades, math_grades, literature_grades, physics_grades, chemistry_grades, student_id, first_name, last_name)
    #     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    #     """
        
    #     with create_connection(database) as conn:
    #         insert_data(conn, sql_query_items, items_data)
    
        # --------------------------------------------------------------------------------------------------
    # with create_connection(database) as conn:
    #     # Дістаємо данні з таблиці students
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT id, first_name, last_name FROM students")
    #     students_data = cursor.fetchall()

    #     # Ділемо студентів на группи
    #     group_size = len(students_data) // 3
    #     group_a = students_data[:group_size]
    #     group_b = students_data[group_size:group_size*2]
    #     group_c = students_data[group_size*2:]
    #     # print("Группа 1:", group_a)
    #     # print("Группа 2:", group_b)
    #     # print("Группа 3:", group_c)
        
    #     # Оновлюємо данні в таблиці groups (назву группи потрібно змінювати вручну)
    #     sql_query_items = """
    #     INSERT INTO groups(student_id, first_name, last_name, group_name)
    #     VALUES (?, ?, ?, 'group_c')
    #     """
        
    #     with create_connection(database) as conn:
    #         insert_data(conn, sql_query_items, group_c)
    pass