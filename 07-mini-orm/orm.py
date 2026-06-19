from dataclasses import dataclass
import sqlite3

DB_NAME = "user.db"

@dataclass
class User:
    name: str
    email: str
    age: int
    id: int = None

    @staticmethod
    def _connect():
        return sqlite3.connect(DB_NAME)

    @staticmethod
    def _create_table():
        conn = User._connect()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL
                )
            ''')
        conn.commit()
        conn.close()

    def save(self):
        conn = User._connect()
        if self.id is None:
            cursor = conn.execute(
                                  "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                (self.name, self.email, self.age)
            )
            self.id = cursor.lastrowid
        else:
            cursor = conn.execute(
                                  "UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?",
                (self.name, self.email, self.age, self.id)
            )
        conn.commit()
        conn.close()

    @classmethod
    def get(cls, user_id):
        conn = cls._connect()
        row = conn.execute(
                           "SELECT id, name, email, age FROM users WHERE id = ?",
            (user_id,)
        ).fetchone()
        conn.close()
        if row is None:
            return None
        return cls(id=row[0], name=row[1], email=row[2], age=row[3])

    def delete(self):
        conn = User._connect()
        conn.execute("DELETE FROM users WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

if __name__ == '__main__':
    User._create_table()

    user = User(name="Alice", email="git@gmail", age=20)
    user.save()
    print(f"Збережено користувача з id={user.id}")

    found = User.get(user.id)
    print(f"Знайдено: {found}")

    found.age = 20
    found.save()
    print("Вік поновлено")

    updated = User.get(user.id)
    print(f"Після оновлення: {updated}")

    updated.delete()
    print("Користувача видалено")

    check = User.get(user.id)
    print(f"Перевірка після видалення: {check}")



