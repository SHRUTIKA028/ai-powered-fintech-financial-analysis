import sqlite3
# =========================================================
# CONNECT TO DATABASE
# =========================================================
conn = sqlite3.connect(
    "finance.db",
    check_same_thread=False
)
cursor = conn.cursor()
# =========================================================
# USER TABLE
# =========================================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()
# =======================================================
# INCOME TABLE
# =========================================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS income(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    source TEXT,
    date TEXT,
    username TEXT
)
""")
conn.commit()
# =========================================================
# EXPENSE TABLE
# =========================================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS expense(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    date TEXT,
    username TEXT
)
""")
conn.commit()
# =========================================================
# BANK IMPORTS TABLE
# =========================================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS bank_imports(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    description TEXT,
    amount REAL,
    type TEXT,
    category TEXT,
    username TEXT
)
""")
conn.commit()
# =========================================================
# REGISTER USER
# =========================================================
def register_user(username, password):
    try:
        cursor.execute(
            """
            INSERT INTO users(username, password)
            VALUES (?, ?)
            """,
            (username, password)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
# =========================================================
# LOGIN USER
# =========================================================
def login_user(username, password):
    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = ?
        AND password = ?
        """,
        (username, password)
    )
    return cursor.fetchone()
# =========================================================
# ADD INCOME
# =========================================================
def add_income(amount, source, date, username):
    cursor.execute(
        """
        INSERT INTO income(
            amount,
            source,
            date,
            username
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            amount,
            source,
            str(date),
            username
        )
    )
    conn.commit()
# =========================================================
# GET USER INCOME
# =========================================================
def get_income(username):
    cursor.execute(
        """
        SELECT id, amount, source, date
        FROM income
        WHERE username = ?
        ORDER BY date
        """,
        (username,)
    )
    return cursor.fetchall()
# =========================================================
# ADD EXPENSE
# =========================================================
def add_expense(amount, category, date, username):
    cursor.execute(
        """
        INSERT INTO expense(
            amount,
            category,
            date,
            username
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            amount,
            category,
            str(date),
            username
        )
    )
    conn.commit()
# =========================================================
# GET USER EXPENSE
# =========================================================
def get_expense(username):
    cursor.execute(
        """
        SELECT id, amount, category, date
        FROM expense
        WHERE username = ?
        ORDER BY date
        """,
        (username,)
    )
    return cursor.fetchall()
# =========================================================
# TOTAL INCOME
# =========================================================
def total_income(username):
    cursor.execute(
        """
        SELECT SUM(amount)
        FROM income
        WHERE username = ?
        """,
        (username,)
    )
    result = cursor.fetchone()[0]
    return result if result else 0
# =========================================================
# TOTAL EXPENSE
# =========================================================
def total_expense(username):
    cursor.execute(
        """
        SELECT SUM(amount)
        FROM expense
        WHERE username = ?
        """,
        (username,)
    )
    result = cursor.fetchone()[0]
    return result if result else 0
# =========================================================
# EXPENSE BY CATEGORY
# =========================================================
def expense_by_category(username):
    cursor.execute(
        """
        SELECT category, SUM(amount)
        FROM expense
        WHERE username = ?
        GROUP BY category
        """,
        (username,)
    )
    return cursor.fetchall()
# =========================================================
# MONTHLY EXPENSES
# =========================================================
def monthly_expenses(username):
    cursor.execute(
        """
        SELECT date, amount
        FROM expense
        WHERE username = ?
        ORDER BY date
        """,
        (username,)
    )
    return cursor.fetchall()
# =========================================================
# MONTHLY EXPENSE SUMMARY
# =========================================================
def monthly_expense_summary(username):
    cursor.execute(
        """
        SELECT
            substr(date, 1, 7) AS month,
            SUM(amount)
        FROM expense
        WHERE username = ?
        GROUP BY month
        ORDER BY month
        """,
        (username,)
    )
    return cursor.fetchall()
## =========================================================
# DELETE USER FINANCIAL DATA
# =========================================================
def delete_user_financial_data(username):
    cursor.execute(
        """
        DELETE FROM income
        WHERE username = ?
        """,
        (username,)
    )
    cursor.execute(
        """
        DELETE FROM expense
        WHERE username = ?
        """,
        (username,)
    )
    conn.commit()
# Change User Password
def change_password(username, new_password):

    cursor.execute(
        """
        UPDATE users
        SET password = ?
        WHERE username = ?
        """,
        (new_password, username)
    )

    conn.commit()

    return cursor.rowcount > 0

# def show_users():
#     cursor.execute("SELECT id, username, password FROM users")
#     return cursor.fetchall()


def reset_password(username, new_password):
    cursor.execute(
        "UPDATE users SET password = ? WHERE username = ?",
        (new_password, username)
    )
    conn.commit()
    return cursor.rowcount > 0


# =========================================================
# DELETE SINGLE EXPENSE
# =========================================================
def delete_expense(expense_id, username):

    cursor.execute(
        """
        DELETE FROM expense
        WHERE id = ?
        AND username = ?
        """,
        (expense_id, username)
    )

    conn.commit()

    return cursor.rowcount > 0
# =========================================================
# DELETE SINGLE INCOME
# =========================================================
def delete_income(income_id, username):

    cursor.execute(
        """
        DELETE FROM income
        WHERE id = ?
        AND username = ?
        """,
        (income_id, username)
    )

    conn.commit()

    return cursor.rowcount > 0
# result = reset_password("shrutika", "Shrutika123")
# print("Password reset result:", result)

# # =========================================================
# # ADD BANK IMPORT
# # =========================================================
# def add_bank_import(
#     date,
#     description,
#     amount,
#     transaction_type,
#     category,
#     username
# ):
#     cursor.execute(
#         """
#         INSERT INTO bank_imports(
#             date,
#             description,
#             amount,
#             type,
#             category,
#             username
#         )
#         VALUES (?, ?, ?, ?, ?, ?)
#         """,
#         (
#             str(date),
#             description,
#             float(amount),
#             transaction_type,
#             category,
#             username
#         )
#     )
#     conn.commit()

# =========================================================
# ADD BANK IMPORT - WITH DUPLICATE CHECK
# =========================================================
def add_bank_import(
    date,
    description,
    amount,
    transaction_type,
    category,
    username
):

    cursor.execute(
        """
        SELECT id
        FROM bank_imports
        WHERE date = ?
        AND description = ?
        AND amount = ?
        AND type = ?
        AND category = ?
        AND username = ?
        """,
        (
            str(date),
            description,
            float(amount),
            transaction_type,
            category,
            username
        )
    )

    existing = cursor.fetchone()

    if existing:
        return False

    cursor.execute(
        """
        INSERT INTO bank_imports(
            date,
            description,
            amount,
            type,
            category,
            username
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            str(date),
            description,
            float(amount),
            transaction_type,
            category,
            username
        )
    )

    conn.commit()

    return True
# =========================================================
# GET BANK IMPORTS
# =========================================================
def get_bank_imports(username):
    cursor.execute(
        """
        SELECT
            date,
            description,
            amount,
            type,
            category
        FROM bank_imports
        WHERE username = ?
        ORDER BY date
        """,
        (username,)
    )
    return cursor.fetchall()