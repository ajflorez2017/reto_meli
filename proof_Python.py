

import pymysql
#import pymysql.connections

#db = pymysql.connect(host="database-1.ckroirhdvbeh.us-east-1.rds.amazonaws.com", user = "admin", password="Reto_2023")

db = pymysql.connect(
    host="database-1.ckroirhdvbeh.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="Reto_2023",
    database="Reto"
)

c = db.cursor()


operation = "I"


match operation:
    case "Ofertar":
        
        # select statement for tblemployee which returns all columns
        Subasta_Update = """UPDATE Subasta_Definition SET Sub_Cur_Value = %s, Sub_Datetime_Last_Offer = %s, WHERE Sub_Id = %s, Sub_Prd_Id = %s;"""

        data = ("00003", "Producto 00003")

        try:
         # Executing the SQL command
   
           c.execute(Subasta_Update, data)
   
         # Commit your changes in the database
           db.commit()

        except:
         # Rolling back in case of error
           db.rollback()

           print("Subasta Updated")


        Subasta_Insert = """UPDATE Subasta_Definition SET Sub_Cur_Value = %s, Sub_Datetime_Last_Offer = %s, WHERE Sub_Id = %s, Sub_Prd_Id = %s;"""  

        data = ("00003", "Producto 00003")

        try:
         # Executing the SQL command
   
           c.execute(Subasta_Insert, data)
   
         # Commit your changes in the database
           db.commit()

        except:
         # Rolling back in case of error
           db.rollback()

           print("Transaccion Insertada")




    
    case "Comprar":
        print("You can become a backend developer")
    
    
    case "S":
        # select statement for tblemployee which returns all columns
        Productos_select = """SELECT * FROM Productos"""

        # execute the select query to fetch all rows
        c.execute(Productos_select)
 
        # fetch all the data returned by the database
        productos_data = c.fetchall()
 
        # print all the data returned by the database
        for e in productos_data:
            print(e)
 
        # finally closing the database connection
        #db.close()

    








# fetch all the data returned by the database
#productos_data = c.fetchall()
 
# print all the data returned by the database
#for e in productos_data:
#    print(e)
 
# finally closing the database connection
db.close()
