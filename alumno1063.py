class categorias:
    #atributos
    id_categoria = 0
    id_producto = 0
    fecha_creacion = ""
    nombre = ""
    descripcion = ""
    estado = ""
    marca = ""

    def mostrar(self):
        print(f"id_categoria: {edgar.id_categoria}, \nid_producto: {edgar.id_producto}, \nfecha de creacion: {edgar.fecha_creacion}, \nnombre: {edgar.nombre}, \ndescripcion: {edgar.descripcion}, \nestado: {edgar.estado}, \nmarca: {edgar.marca}")
    def  lista_categ(self):
        lis_cat=[1432,5618,"7 de enero de 2024","tenis superdeportivos ","tenis todoterreno para correr","nuevos","nike"]
        for x in lis_cat:
            print(x)
    def tupla_categ(self):
        tupla_cat = (1432,5618,"7 de enero de 2024","tenis superdeportivos ","tenis todoterreno para correr","nuevos","nike")
        for x in tupla_cat:
            print(x)
    def diccionario_categ(self):
        dicc_cat = {
                    "id categoria: ": 1432,
                    "id producto: ": 5618,
                    "fecha de creacion ": "7 de enero de 2024",
                    "nombre ": "tenis superdeportivos",
                    "descripcion ": "tenis todoterreno para correr",
                    "estado ": "nuevos",
                    "marca ": "nike"}
        for x, y in dicc_cat.items():
            print(x,y)
    def alta_cat(self):
        print("se dio de alta la categoria")
    def baja_cat(self):
        print("se dio de baja la categoria")

edgar= categorias()

edgar.id_categoria =1432
edgar.id_producto =5618
edgar.fecha_creacion ="7 de enero de 2024"
edgar.nombre ="tenis superdeportivos"
edgar.descripcion ="tenis todoterreno para correr"
edgar.estado ="nuevos"
edgar.marca ="nike"

print("mostrando datos")
edgar.mostrar
print("")
print("lista de categorias")
edgar.lista_categ()
print("")
print("tupla de categorias")
edgar.tupla_categ()
print("")
print("diccionario de categorias")
edgar.diccionario_categ()
print("")
print("alta de categorias")
edgar.alta_cat()
print("")
print("baja de categorias")
edgar.baja_cat()


