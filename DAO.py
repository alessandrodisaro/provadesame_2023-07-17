from database.DBConnect import DBConnect


class DAO():
    def __init__(self):
        pass



    @staticmethod
    def getColori():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct(Product_color) from go_products gp """
        cursor.execute(query)

        results = []

        for row in cursor:
            results.append(row["Product_color"])

        cursor.close()
        cnx.close()

        return results

    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct(year(Date))
                    from go_daily_sales gds  """
        cursor.execute(query)

        results = []

        for row in cursor:
            results.append(row["distinct(year(Date))"])

        cursor.close()
        cnx.close()

        return results





