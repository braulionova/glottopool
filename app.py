from flask import Flask, render_template, jsonify, make_response, json, request
import pymysql.cursors
import numpy as np
import pickle

app = Flask(__name__)

#conexion db
connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='euphratis',
                                 db='glottopool',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.Cursor)

#main
@app.route('/')
def main():
    return render_template("index.html")


#/generar/leidsa/lotto
@app.route('/generar/leidsa/lotto')
def generar_lotto():
    return render_template("lotto.html")

@app.route('/api/leidsa/lotto/generator/add', methods=['POST'])
def service():
    data = json.loads(request.data)
    #data = json.dumps(data)
    #text = data.get("text",None)

    if(data):
        for row in data:
            execres(connection, "insert into generador_lotto_leidsa (fecha, comb1, comb2, comb3, comb4, comb5, comb6, extra1, extra2, jackpotcomp) VALUES ('" 
            + row['fecha']  + "'," + row['comb1']  + "," + row['comb2']  + "," + row['comb3'] + "," + row['comb4'] + "," + row['comb5'] 
            + "," + row['comb6'] + "," + row['extra1'] + "," + row['extra2'] + ",'" + row['jackpotcomp'] + "')")
        return "{200, Data Procesed.}"
    else:
        return 'nothing'

    #if text is None
    #    return jsonify({"message":"text not found"})
    #else:
    #    execres(connection, "insert into generador_lotto_leidsa (fecha, comb1, comb2, comb3, comb4, comb5, comb6, extra1, extra2, jackpotcomp) VALUES ('2020-03-24', '02', '03', '04', '05', '06', '07', '01', '09', 'RD$ 304 MM')")
    #    #tableset(connection, 'generador_lotto_leidsa', 'fecha, comb1, comb2, comb3, comb4, comb5, comb6, extra1, extra2, jackpotcomp', ["24-03-2020", "02", "03", "04", "05", "06", "07", "01", "09", "RD$ 304 MM"])
    #    return jsonify(data)

@app.route('/api/leidsa/lotto/generator/all')
def get_all_lotto_leidsa():
    RES_DB = tableselect(connection, 'generador_lotto_leidsa', 'id_generador_lotto_leidsa, comb1, comb2, comb3, comb4, comb5, comb6, extra1, extra2, jackpotcomp')
    lista_db = RES_DB.tolist()
    data = json.dumps(lista_db)
    return data
#execres
def execres(conn,sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    res = cursor.fetchall()
    cursor.close()
    return res

def tableselect(*args):
    #### --- función de lectura a db ---- ###
    #--- Necesita una declaración del cursor db sólo como: 'Cursor'
    #--- Necesita la librería NumPy

    #--- params
    narg = len(args)
    conn=args[0]
    table=args[1]
    if narg < 3:
        fields = []
        condition = []
    elif narg < 4:
        fields = args[2]
        condition = []
    else:
        fields = args[2]
        condition = args[3]
    #--- preguntar si la tabla existe
    schemas=str(connection.db)
    schemas=schemas[2:len(schemas)-1]
    res=execres(conn,"SHOW TABLES FROM " + schemas + " LIKE '" + table + "'")
    if res: #--- si hay tablas
        rex=str(res[0])
        if rex.find(table): #--- si está la tabla de entrada
            #--- pregunta primary key
            res = execres(conn,'show columns from ' + table + ' where `Key` = "PRI";')
            PK=[]
            #--- si hay primary Key
            if res:
                rex = list(res[0])
                PK = str(rex[0])
            else:
                #--- si NO hay primary Key
                res = execres(conn,"SELECT COLUMN_NAME, EXTRA FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '" + schemas + "' AND TABLE_NAME = '" + table + "'")
                if type(res) is tuple:
                    for i in range(0, len(res)):
                        ext=res[i][1]
                        if ext.lower() == 'auto_increment':
                            PK=res[i][0]
            #--- si hay campos
            if fields:
                if type(fields) is list:
                    fieldx = fields
                    cmp=','
                    fields=cmp.join(fields)
                else:
                    fieldx = fields.split(',')
                #--- trim
                fieldx = list(map(str.strip, fieldx))
                #---
                if not condition:
                    if not PK:
                        sql = "SELECT " + fields + " FROM " + table
                    else:
                        sql = "SELECT " + fields + " FROM " + table + " ORDER BY " + PK + " ASC"
                else:
                    if not PK:
                        sql = "SELECT " + fields + " FROM " + table + " WHERE " + condition
                    else:
                        sql = "SELECT " + fields + " FROM " + table + " WHERE " + condition + " ORDER BY " + PK + " ASC"
            else:
                #--- si NO hay campos
                res = execres(conn,"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '" + schemas + "' AND TABLE_NAME = '" + table + "'")
                if type(res) is tuple:
                    fieldx=list()
                    for i in range(0, len(res)):
                        fieldx.append(res[i][0])
                #---
                if not condition:
                    if not PK:
                        sql = "SELECT * FROM " + table
                    else:
                        sql = "SELECT * FROM " + table + " ORDER BY " + PK + " ASC"
                else:
                    if not PK:
                        sql = "SELECT * FROM " + table + " WHERE " + condition
                    else:
                        sql = "SELECT * FROM " + table + " WHERE " + condition + " ORDER BY " + PK + " ASC"
            #--- llamada exec principal
            values = execres(conn,sql)
            #---- reconstruccion
            res = np.asmatrix(values,np.ndarray)
            return res
        else:
            return 'No table'
    else:
        return 'No table'

def tableset(*args):
    #### --- función de escritura a db ---- ###
    #--- Necesita una declaración del cursor db sólo como: 'Cursor'
    #--- Necesita la librería NumPy

    status=0
    finsert = 0
    #--- params
    narg = len(args)
    conn = args[0]
    table = args[1]
    if narg < 3:
        fields = []
        value=[]
        condition = []
    elif narg < 4:
        fields = args[2]
        value=[]
        condition = []
    elif narg < 5:
        fields = args[2]
        value = args[3]
        condition = []
    else:
        fields = args[2]
        value = args[3]
        condition = args[4]
    #--- format fields
    if type(fields) is list:
        fieldx = fields
        cmp = ','
        fields = cmp.join(fields)
    else:
        fieldx = fields.split(',')
    #--- trim
    fieldx=list(map(str.strip,fieldx))
    #print(fieldx)
    #--- schema
    schemas=str(connection.db)
    schemas=schemas[2:len(schemas)-1]
    #print('data = ' + str(np.shape(value)))
    #--- dim checks
    dt=type(value)
    #print('TYPE = ' + str(type(value)))
    if dt == int or dt == float:
        #print('>> INT')
        value = np.asmatrix(value)
        #print(value)
    elif dt == str:
        #print('>> STR')
        valuex = np.asmatrix(1,np.ndarray)
        valuex[0]="'" + value + "'"
        value=valuex
        #print(value)
    elif dt == list:
        #print('>> LIST')
        value = np.asmatrix(value,np.ndarray)
        #print(value)
    #elif dt == np.ndarray:
        #print('>> ARRAY')
    #elif dt == np.matrixlib.defmatrix.matrix:
        #print('>> MATRIX')
    #--- selector de dims
    NHS = np.shape(value)
    #print(NHS)
    NH=NHS[0]
    NW=NHS[1]
    #print('NH = ' + str(NH)+ ' | NW = ' + str(NW))
    #--- si es multi-dimensional
    if NH > 1:
        a=1
        #--- si es un vector
        if NW == 1:
            a = 1
        # --- si es una matriz
        else:
            a = 1
    #--- si es una dimension
    else:
        #--- si es un valor
        NC = len(fieldx)
        #print('NC= ' + str(NC))
        if NW==1:
            if NC > 1: #--- varios campos
                a=1
                #---si son varios valores
            else:   #--- un solo campo
                if not condition:
                    sql='UPDATE ' + schemas + '.' + table + ' SET ' + fields + '=' + str(value[0,0])
                else:
                    sql='UPDATE ' + schemas + '.' + table + ' SET ' + fields + '=' + str(value[0,0]) + ' where ' + condition
                #print(sql)
        else: #--- si es una sección de registro (varios valores)
            if NC != NW:
                print('* Error de dimensiones entre los campos y valores a insertar.')
                return status
            #--- si hay data
            res=execres(conn,'SELECT EXISTS(SELECT 1 FROM ' + table + ')')
            if max(res[0]):
                multfields = str()
                for n in range(0,NC):
                    if type(value[0,n])==str:
                        multfields = multfields + str.strip(fieldx[n]) + "='" + value[0,n] + "',"
                    else:
                        v=value[0,n]
                        #print(v)
                        if v==():
                            datas='NULL'
                        else:
                            datas=str(v)
                        multfields = multfields + str.strip(fieldx[n]) + '=' + datas + ','
                multfields=multfields[0:-1]
                if not condition:
                    sql = 'UPDATE ' + schemas + '.' + table + ' SET ' + multfields
                else:
                    sql = 'UPDATE ' + schemas + '.' + table + ' SET ' + multfields + ' where ' + condition
                #print(sql)
            else: #--- si la tabla está vacía
                finsert=1
                return status
    if not finsert:
        #--- habilitar update
        execres(conn,'SET SQL_SAFE_UPDATES=0')
        #--- escribir
        execres(conn,sql)
        #--- Deshabilitar Update
        execres(conn,'SET SQL_SAFE_UPDATES=1')
    else:
        a=1
    status=1
    return status

#tableset
def tableset(*args):
    #### --- función de escritura a db ---- ###
    #--- Necesita una declaración del cursor db sólo como: 'Cursor'
    #--- Necesita la librería NumPy

    status=0
    finsert = 0
    #--- params
    narg = len(args)
    conn = args[0]
    table = args[1]
    if narg < 3:
        fields = []
        value=[]
        condition = []
    elif narg < 4:
        fields = args[2]
        value=[]
        condition = []
    elif narg < 5:
        fields = args[2]
        value = args[3]
        condition = []
    else:
        fields = args[2]
        value = args[3]
        condition = args[4]
    #--- format fields
    if type(fields) is list:
        fieldx = fields
        cmp = ','
        fields = cmp.join(fields)
    else:
        fieldx = fields.split(',')
    #--- trim
    fieldx=list(map(str.strip,fieldx))
    #print(fieldx)
    #--- schema
    schemas=str(conn.db)
    schemas=schemas[2:len(schemas)-1]
    #print('data = ' + str(np.shape(value)))
    #--- dim checks
    dt=type(value)
    #print('TYPE = ' + str(type(value)))
    if dt == int or dt == float:
        #print('>> INT')
        value = np.asmatrix(value)
        #print(value)
    elif dt == str:
        #print('>> STR')
        valuex = np.asmatrix(1,np.ndarray)
        valuex[0]="'" + value + "'"
        value=valuex
        #print(value)
    elif dt == list:
        #print('>> LIST')
        value = np.asmatrix(value,np.ndarray)
        #print(value)
    #elif dt == np.ndarray:
        #print('>> ARRAY')
    #elif dt == np.matrixlib.defmatrix.matrix:
        #print('>> MATRIX')
    #--- selector de dims
    NHS = np.shape(value)
    #print(NHS)
    NH=NHS[0]
    NW=NHS[1]
    #print('NH = ' + str(NH)+ ' | NW = ' + str(NW))
    #--- si es multi-dimensional
    if NH > 1:
        a=1
        #--- si es un vector
        if NW == 1:
            a = 1
        # --- si es una matriz
        else:
            a = 1
    #--- si es una dimension
    else:
        #--- si es un valor
        NC = len(fieldx)
        #print('NC= ' + str(NC))
        if NW==1:
            if NC > 1: #--- varios campos
                a=1
                #---si son varios valores
            else:   #--- un solo campo
                if not condition:
                    sql='UPDATE ' + schemas + '.' + table + ' SET ' + fields + '=' + str(value[0,0])
                else:
                    sql='UPDATE ' + schemas + '.' + table + ' SET ' + fields + '=' + str(value[0,0]) + ' where ' + condition
                #print(sql)
        else: #--- si es una sección de registro (varios valores)
            if NC != NW:
                print('* Error de dimensiones entre los campos y valores a insertar.')
                return status
            #--- si hay data
            res=execres(conn,'SELECT EXISTS(SELECT 1 FROM ' + table + ')')
            if max(res[0]):
                multfields = str()
                for n in range(0,NC):
                    if type(value[0,n])==str:
                        multfields = multfields + str.strip(fieldx[n]) + "='" + value[0,n] + "',"
                    else:
                        v=value[0,n]
                        #print(v)
                        if v==():
                            datas='NULL'
                        else:
                            datas=str(v)
                        multfields = multfields + str.strip(fieldx[n]) + '=' + datas + ','
                multfields=multfields[0:-1]
                if not condition:
                    sql = 'UPDATE ' + schemas + '.' + table + ' SET ' + multfields
                else:
                    sql = 'UPDATE ' + schemas + '.' + table + ' SET ' + multfields + ' where ' + condition
                #print(sql)
            else: #--- si la tabla está vacía
                finsert=1
                return status
    if not finsert:
        #--- habilitar update
        execres(conn,'SET SQL_SAFE_UPDATES=0')
        #--- escribir
        execres(conn,sql)
        #--- Deshabilitar Update
        execres(conn,'SET SQL_SAFE_UPDATES=1')
    else:
        a=1
    status=1
    return status