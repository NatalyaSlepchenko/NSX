import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\stud\Downloads\Для курсовой 2.accdb;'
    conn = pyodbc.connect(con_string)

    cursor = conn.cursor()
    Расписание =(
        (6, '15', 'Вип-зал'),
        (7, '85', 'Стандарт'),
        (8, '25', 'Комфорт'),
    )

    cursor.executemany('INSERT INTO Расписание VALUES (?,?,?)', Расписание)
    conn.commit()
    print('Data Inserted')

except pyodbc.Error as e:
    print("Error in connection", e)