# from utils.db_api.sqlite import Database
#
# db = Database()
#
# def test():
#     db.create_table_users()
#     users = db.select_all_user()
#     print(f"До добавления пользователей: {users=}")
#     db.add_user(1, "One", "email")
#     db.add_user(2, "Vasya", "email")
#     db.add_user(3, "1", "1")
#     db.add_user(4, "1", "1")
#     db.add_user(5, "John", "john@mail.com")
#     users = db.select_all_user()
#     print(f"После добавления пользователей: {users=}")
#     user = db.select_user(Name="John", id=5)
#     print(f"Получил пользователя {user}")
#
# test()