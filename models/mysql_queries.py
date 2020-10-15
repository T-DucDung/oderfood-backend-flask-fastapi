import mysql
import sys

from ..config.model_global import get_mysql_connection


def execute_select_first_value(select_query: str):
    """
    select ra gia tri list[0][0]
    :param select_query:
    :return:
    """
    connection = get_mysql_connection()
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(select_query)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        if rows:
            result = rows[0][0]
        return result
    except (Exception) as error:
        message = f"execute_select_first_value error {error}"
        connection.rollback()
        print(select_query)
        return send_abort(code=400, message=message)
    finally:
        cursor.close()
        connection.close()


def execute_count_query(count_query) -> int:
    """
    - Thực thi câu count query
    :param count_query:
    :param connection: postgre connection
    :return: hàng 1, cột 1 của dữ liệu
    """
    connection = get_mysql_connection()
    cursor = connection.cursor()
    count = 0
    try:
        cursor.execute(count_query)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        print('COUNT QUERY', rows[0][0])
        count = rows[0][0]
    except (Exception) as error:
        print("execute_count_query error")
        connection.rollback()
        cursor.close()
        connection.close()
        print(error)

    return count


def execute_select_query(select_query: str) -> []:
    """
    Execute select query in POSTGRE
    :param select_query:
    :param connection: postgre connection
    :return: Mảng các giá trị dict hoặc []
    """
    connection = get_mysql_connection()
    cursor = connection.cursor()
    result = []
    try:
        cursor.execute(select_query)
        cols_description = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        if rows is None or len(rows) == 0:
            return None
        for row in rows:
            data = {}  # dữ liệu của một bản ghi
            for index, value in enumerate(row):
                data[cols_description[index]] = value
            result.append(data)

    except(Exception) as error:
        print("execute_select_query error", error)
        connection.rollback()
        cursor.close()
        connection.close()
        # send_abort(code=400, message="execute_select_query error")
    return result


def execute_none_query(query):
    """
        Sử dụng cho POST, DELETE, UPDATE
        Thực thi một câu query và không trả về gì,
    """
    connection = get_mysql_connection()
    cursor = connection.cursor()
    result = {}
    print(query)
    try:
        cursor.execute(query)
        connection.commit()
        connection.close()
        result['data'] = True
    except (Exception) as error:
        print("execute_none_query error", error)
        print('\t SQL: ', query)
        connection.rollback()
        cursor.close()
        connection.close()
    return result


# execute_none_query("INSERT INTO User( user_name, full_name, image_url, address, mobile, email, created_date, password, image_path,status)VALUES ( 'BUINHULAC123', 'BUI NHU LAC', 'ABC', 'ABCSD', '0987654321', 'SONNAM@GMAIL.COM', '2018-01-09', 'ABC123','ASDFG',1);")
print(execute_select_first_value("select count(*) from USER"))
