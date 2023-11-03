# import sqlite3
#
# conn = sqlite3.connect('../db.sqlite3')
# cursor = conn.cursor()
#
# select_query = "SELECT id, book_date from fivecart_book"
# cursor.execute(select_query)
# data_to_insert = cursor.fetchall()

# for row in data_to_insert:
#     cursor.execute("UPDATE fivecart_book SET book_date = SELECT book_date")

# alter_query = """
# ALTER TABLE fivecart_book
# ALTER COLUMN book_date TYPE DATE USING TO_DATE(date_column, 'YYYY/MM/DD')
# """
# cursor.execute(alter_query)
# conn.commit()
#
# conn.close()


#
# # select_query = "SELECT DISTINCT book_writer from fivecart_total_pre"
# # select_query = """
# # SELECT DISTINCT f.title, b.id, c.id, f.book_date, f.is_classic
# # from fivecart_total_pre f
# # INNER JOIN fivecart_company c ON f.book_company = c.company_name
# # INNER JOIN fivecart_bookwriter b ON f.book_writer = b.book_writer
# # """
# select_query = """
# SELECT f.date_writer, f.report_text, u.id, b.id
# from fivecart_total_pre f
# INNER JOIN fivecart_book b on f.title = b.title and f.book_date = b.book_date
# INNER JOIN fivecart_user u on f.report_writer = u.user_name
# WHERE NOT f.report_text is NULL;
# """
# # delete_query = "delete from fivecart_book"
#
# cursor.execute(select_query)
# data_to_insert = cursor.fetchall()
#
#
# for row in data_to_insert:
#     cursor.execute("INSERT INTO fivecart_report (report_date, report_text, user_id, book_id) VALUES (?,?,?,?)", (row[0], row[1], row[2], row[3],))
#
# # for row in data_to_insert:
# #     cursor.execute("INSERT INTO fivecart_company (company_name) values (?)", (row[0],))
#
# conn.commit()
#
# conn.close()
