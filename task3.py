import sqlite3
from datetime import datetime, date
from email.message import EmailMessage


class User:
    def __init__(self, first_name, last_name, middle_name, email, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.email = email
        self.birthday = birthday

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_short_name(self):
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."

    def get_age(self):
        today = datetime.now().date()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age

    def __str__(self):
        return f"{self.get_full_name()} ({self.birthday})"


def register_user(user):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                    first_name text,
                    last_name text,
                    middle_name text,
                    email text,
                    birthday text
                )""")
    c.execute("INSERT INTO users VALUES (?,?,?,?,?)", (user.first_name, user.last_name, user.middle_name, user.email, user.birthday))
    conn.commit()
    conn.close()
    send_email(user.email)


def send_email(email):
    message = EmailMessage()
    message['Subject'] = 'Thank you for registering'
    message['From'] = 'noreply@example.com'
    message['To'] = email
    message.set_content('Thank you for registering!')
    # The following line is just for demonstration purposes and wouldn't actually send an email
    print(message)


def search_user(query):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE first_name=? OR last_name=? OR email=?", (query, query, query))
    results = c.fetchall()
    conn.close()
    return results


Vadim = User("Vadim", "Liubin", "Arkadievich", "vadart@mail.com", date(1985, 8, 7))
register_user(Vadim)
print(Vadim.get_age())
print(Vadim.get_short_name())
print(Vadim.get_full_name())


