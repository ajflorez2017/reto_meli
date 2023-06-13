
# Importar módulos requeridos

import pymysql

# --------------------------------------------------------------------------------------------------------
# offer(Cur_Value, DateLastOffer, SubastaId, ProductoId)
# ------------------------------------------------------
# Funcion que se encarga de registrar la oferta que se hace por un producto dentro de una subasta
# Recibe los siguientes parametros:
#     - Cur_Value: Valor de la oferta que a su vez se convierte en el valor actual del producto
#     - DateLastOf: Fecha/Hora de la oferta, se toma en la pagina la fecha hora del sistema
#     - SubastaId: Identificación/Id/Consecutivo de la subasta, viene desde la pagina.
#     - ProductoId: Identificación/Código del producto
#
#
#
#
#        
def offer(Cur_Value, DateLastOffer, SubastaId, ProductoId, xTrx_Id,  xTrx_cli_id, xTrx_value_Offer, xTrx_date, xtrx_time):
        

    # Definición de la conexión a la base de datos

    db = pymysql.connect(
                        host="database-1.ckroirhdvbeh.us-east-1.rds.amazonaws.com",
                        user="xxxxxx",
                        passwd="xxxxxxxxx",
                        database="Reto"
                        )

    c = db.cursor()

    # 
    # Se actualiza el registro de la subasta con el último valor y la fecha/hora para los controles
    #      
    Subasta_Update = """UPDATE Subasta_Definition SET Sub_Cur_Value = %s, Sub_Datetime_Last_Offer = %s, WHERE Sub_Id = %s, Sub_Prd_Id = %s;"""

    data = (Cur_Value, DateLastOffer, SubastaId, ProductoId)

    try:
       # Ejecuta el comando SQL
   
       c.execute(Subasta_Update, data)
   
       # Se confirman los cambios en la base de datos
       db.commit()

    except:
         # Se devuelven los cambios si ocurre algún error
         db.rollback()

    # 
    # Se adiciona un registro en el log transacciones 
    #   
    Subasta_Insert = """INSERT INTO Reto.Transacciones(Trx_Id, Trx_Prd_Id, Trx_Sub_Id, Trx_cli_id, Trx_value_Offer, Trx_date, trx_time)
                               VALUES(%s, %s, %s, %s, %s, %s, %s);"""  


    xTrx_Prd_Id = ProductoId
    xTrx_Sub_Id = SubastaId    

    data = (xTrx_Id, xTrx_Prd_Id, xTrx_Sub_Id, xTrx_cli_id, xTrx_value_Offer, xTrx_date, xtrx_time)

    try:
       # Ejecuta el comando SQL
   
       c.execute(Subasta_Insert, data)
   
       # Se confirman los cambios en la base de datos
       db.commit()
       print("Transaccion Insertada")

    except:
         # Se devuelven los cambios si ocurre algún error
         db.rollback()

        

# --------------------------------------------------------------------------------------------------------
# buy(Cur_Value, DateLastOffer, SubastaId, ProductoId, xTrx_Id, xTrx_cli_id, xTrx_value_Offer, xTrx_date, xtrx_time)
# ------------------------------------------------------
# Funcion que se encarga de registrar la compra de un producto en el archivo de transacciones y cierra la subasta del item o producto
# Recibe los siguientes parametros:
#     - Cur_Value: Valor de la oferta que a su vez se convierte en el valor actual del producto
#     - DateLastOf: Fecha/Hora de la oferta, se toma en la pagina la fecha hora del sistema
#     - SubastaId: Identificación/Id/Consecutivo de la subasta, viene desde la pagina.
#     - ProductoId: Identificación/Código del producto
#
#
#
#
#        
def buy(Cur_Value, DateLastOffer, SubastaId, ProductoId, xTrx_Id, xTrx_cli_id, xTrx_value_Offer, xTrx_date, xtrx_time):
        
    #
    # Definición de la conexión a la base de datos
    #

    db = pymysql.connect(
                        host="database-1.ckroirhdvbeh.us-east-1.rds.amazonaws.com",
                        user="xxxxxx",
                        passwd="xxxxxxxxx",
                        database="Reto"
                        )

    c = db.cursor()

    # 
    # Se actualiza el registro de la subasta con el último valor y la fecha/hora para los controles
    #      
    Subasta_Update = """UPDATE Subasta_Definition SET Sub_Cur_Value = %s, Sub_Datetime_Last_Offer = %s, Sub_Status = %s WHERE Sub_Id = %s, Sub_Prd_Id = %s;"""

    data = (Cur_Value, DateLastOffer, "C", SubastaId, ProductoId)

    try:
       # Ejecuta el comando SQL
   
       c.execute(Subasta_Update, data)
   
       # Se confirman los cambios en la base de datos
       db.commit()

    except:
         # Se devuelven los cambios si ocurre algún error
         db.rollback()

    # 
    # Se adiciona un registro en el log transacciones 
    #   
    Subasta_Insert = """INSERT INTO Reto.Transacciones(Trx_Id, Trx_Prd_Id, Trx_Sub_Id, Trx_cli_id, Trx_value_Offer, Trx_date, trx_time)
                               VALUES(%s, %s, %s, %s, %s, %s, %s);"""  


    xTrx_Prd_Id = ProductoId
    xTrx_Sub_Id = SubastaId    

    data = (xTrx_Id, xTrx_Prd_Id, xTrx_Sub_Id, xTrx_cli_id, xTrx_value_Offer, xTrx_date, xtrx_time)

    try:
       # Ejecuta el comando SQL
   
       c.execute(Subasta_Insert, data)
   
       # Se confirman los cambios en la base de datos
       db.commit()
       print("Transaccion Insertada")

    except:
         # Se devuelven los cambios si ocurre algún error
         db.rollback()

        

