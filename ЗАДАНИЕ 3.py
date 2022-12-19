import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\stud\Downloads\Для курсовой 2.accdb'
    conn = pyodbc.connect(con_string)

    Расписание_ID = 2

    cur = conn.cursor()
    cur.execute('DELETE FROM Расписание WHERE id = ?', (Расписание_ID))
    conn.commit()
    print("Data Deleted ")

except pyodbc.Error as e:
    print("Error in Connection")
