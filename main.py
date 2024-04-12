import os
from connection import create_connection, database

from pprint import pprint

# ok
# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
request_1 = 'request_from_msql/request_1.sql'

# ok
# Знайти студента із найвищим середнім балом з певного предмета. Щоб вобрати предмет, додайте аргумент до функціі(math, history, literature, physics, chemistry). Приклад request_from_sql(request_2, 'math')
request_2 = 'request_from_msql/request_2.sql'

# ok
# Знайти середній бал у групах з певного предмета. Приклад request_from_sql(request_3,subject='history_grades', group_name='group_c')
request_3 = 'request_from_msql/request_3.sql'

# ok
# Знайти середній бал на потоці (по всій таблиці оцінок).
request_4 = 'request_from_msql/request_4.sql'

# ok
# Знайти які курси читає певний викладач. ВВедіть його ИД. Приклад request_from_sql(request_5, '2')
request_5 = 'request_from_msql/request_5.sql'

# ok
# Знайти список студентів у певній групі. Приклад request_from_sql(request_6, 'group_b')
request_6 = 'request_from_msql/request_6.sql'

# ok
# Знайти оцінки студентів у окремій групі з певного предмета. Приклад request_from_sql(request_7,subject='history_grades', group_name='group_b')
request_7 = 'request_from_msql/request_7.sql'

# ok
# Знайти середній бал, який ставить певний викладач зі своїх предметів. ВВедіть його ИД. Приклад request_from_sql(request_8, teacher_id=2)
request_8 = 'request_from_msql/request_8.sql'

# ok
# Знайти список курсів, які відвідує студент.ВВедіть ИД студента. Приклад request_from_sql(request_9, '9')
request_9 = 'request_from_msql/request_9.sql'

# ok
# Список курсів, які певному студенту читає певний викладач. Приклад request_from_sql(request_10, student_id= 11, teacher_id= 3)
request_10 = 'request_from_msql/request_10.sql'


# Створення шляху до файлу з використанням os.path.join()
request_1_path = os.path.join(os.path.dirname(__file__), request_1)
def request_from_sql(sql_file, subject=None, item=None, teacher_id=None, student_id=None, group_name=None):
    with open(sql_file, 'r', encoding='utf-8') as file:
        sql_query = file.read()
        if subject == 'group_a' or subject == 'group_b' or subject == 'group_c':
            sql_query = sql_query.replace('{subject}', f"'{subject}'")
        elif subject:
            sql_query = sql_query.replace('{subject}', subject)
            
    with create_connection(database) as conn:
        cursor = conn.cursor()
        if teacher_id is not None and student_id is not None:
            cursor.execute(sql_query, (student_id, teacher_id))
        elif item is not None and group_name is not None:
            cursor.execute(sql_query, (item, group_name))
        elif group_name is not None and subject is not None:
            cursor.execute(sql_query, (group_name, ))
        elif teacher_id:
            cursor.execute(sql_query, (teacher_id, ))
        else:
            cursor.execute(sql_query)
        data = cursor.fetchall()
        pprint(data)



if __name__ == "__main__":
    request_from_sql(request_10, student_id= 11, teacher_id= 3)