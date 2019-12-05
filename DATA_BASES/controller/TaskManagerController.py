import DATA_BASES.sql.database_credentials as secret
import pymysql

from DATA_BASES.model.Task import Task
from DATA_BASES.model.User import User

class TaskManagerController:
    users = [] # koresponduje z rekordami w tabelce user
    def __init__(self):
        self.connection = pymysql.connect(
            secret.host,
            secret.username,
            secret.password,
            db=secret.database_name,
            charset = 'utf8',
            port=3306
        )
        print(' ... CONNECTED ...')
        self.cursor = self.connection.cursor()

    def insertUser (self, email, password, name, lastname, gender):
        u = User(email, password, name, lastname, gender)
        self.cursor.execute("INSERT INTO user VALUES (default, %s, %s, %s, %s, %s)",
                            (u.email, u.password, u.name, u.lastname, u.gender))
        print("DODANO uzytkownika", u.email)
        if (input("Czy na pewno chcesz dodać: " + u.email + "(T/N)").upper() == "T"):
            self.connection.commit()         # potwierdzenie transakcji
            print('DODANO', u.email)
        else:
            self.connection.rollback()     # odrzucenie transakcji
            print('NIE DODANO', u.email)

    def selectUsers(self):
# wykonanie zapytania sql -> zwraca wynik
        self.cursor.execute("SELECT * FROM user")
        result = self.cursor.fetchall()  # pobieramy wszystkie wyniki
        for row in result:
            u = User(row[1], row[2], row[3], row[4], row[5], row[0])
            print(u)

    def insertTaskToUser(self, name, description, status, date_stop, user_number):
        t = Task(name, description, status, date_stop, user_number)
        self.cursor.execute('INSERT INTO tasks VALUES (default, %s, %s, %s, %s, default, %s)',
                            (t.user_number, t.name, t.description, t.status, t.date_stop, ))
        self.connection.commit()
        print("DODANO ZADANIE", t.name)

    def selectTasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        for row in self.cursor.fetchall():
            t = Task(row[1], row[2], row[3], row[5], row[6], row[0], row[4])
            print(t)
    def selectSummary (self):
        self.cursor.execute('SELECT * FROM summary')
        for row in self.cursor.fetchall():
            print("| %s | %s | %s | %s | %s | %s | %s |" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    def updateTaskDateStop(self, task_number, newDeadline):
        self.cursor.execute("UPDATE tasks SET date_stop = %s WHERE task_number = %s", (newDeadline, task_number))
        self.connection.commit()
        self.selectTasks()