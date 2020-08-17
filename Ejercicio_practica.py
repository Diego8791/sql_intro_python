import csv
import sqlite3


def create_schema():
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    
    c.execute("""
            DROP TABLE IF EXISTS libreria;
            """)
    
    c.execute("""
            CREATE TABLE lista_libros (
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [title] TEXT NO NULL,
                [pags] INTEGER NO NULL,
                [author] TEXT NO NULL
                );
                """)
    
    conn.commit()
    conn.close()


def fill():
    # Apertura de base de datos 
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    
    # Apertura de archivo csv
    with open('libreria.csv') as csvfile:
        data = list(csv.reader(csvfile))
    
    #lectura de archivo data e ingreso de datos a table lista_libros
    for x in range(len(data)):
        if x > 0:
            c.execute("""
                    INSERT INTO lista_libros (title, pags, author)
                    VALUES (?,?,?);""", data[x])

    conn.commit()
    conn.close()


def fetch(id):
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()

    if id == 0:
        c.execute("SELECT * FROM lista_libros")
        data = c.fetchall()
        print(data)
    else:
        for row in c.execute('SELECT * FROM lista_libros WHERE id=?', (id,)):
            print(row)

    conn.commit()
    conn.close()


def search_author(titulo):
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    
    for row in c.execute("SELECT (author) FROM lista_libros WHERE title=?", (titulo,)):
        print(row)
    
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Crear DB
    # create_schema()

    # Completar la DB con el CSV
    # fill()

    # Leer filas
        
    fetch(0)  # Ver todo el contenido de la DB
    fetch(3)  # Ver la fila 3
    fetch(20)  # Ver la fila 20

    # Buscar autor
    # print(search_author('Relato de un naufrago'))
    search_author('Relato de un naufrago')