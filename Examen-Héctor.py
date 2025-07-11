 #Hola papus, hoy vamos a morir chicos sin embargo aun tenemos fe en nuestros corazones... !!SHINSOO SASAGEYOOOOO¡¡
 # {:[V Mexicano
 
 #Funciones
 
 #Funcion para Stock
def stock_marca(marca):
    total = 0
    for codigo, datos in productos.items():
        if datos[0].lower() == marca:
            total += stock[codigo][1]
    print(f"El stock que tenemos para {marca} es de: {total}")        
                    
def búsqueda_precio(p_min, p_max):
    resultados_busqueda = []
    for codigo, datos in productos.items():
        precio = stock[codigo][0]
        if precio >= p_min and precio <= p_max and stock[codigo][1] > 0 :
            resultados_busqueda.append(datos[0] + "---" + codigo)
        if resultados_busqueda:
            resultados_busqueda.sort()
        else:
            print("No hay notebooks en ese rango de precios.")
    print(f"Productos Encontrados: {resultados_busqueda}")

def actualizar_precio(modelo,p):
    for codigo in stock:
        if modelo in stock:
            stock[modelo][0] = p
    if modelo not in stock:         
        print("No existe dicho modelo")
        return False 
    print("Precio actualizado!!")          
    return True       
#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
    }
def main():    
    while True:
        while True:
            try:
                print("\n***MENU PRINCIPAL***")
                opc = int(input("1. Stock marca. \n2. Búsqueda por precio. \n3. Actualizar precio. \n4. Salir. \nIngrese una opcion: "))
                break
            except ValueError:
                print("\n!!ERROR¡¡\nSolo se permiten numeros enteros")
        if opc == 1:
            marca = input("Ingrese la marca para conocer el stock de esta: ").lower()
            stock_marca(marca)
        elif opc == 2:
            while True:
                try:
                    p_min = int(input("Ingrese el precio minimo: "))
                    p_max = int(input("Ingrese el precio maximo: "))
                    búsqueda_precio(p_min, p_max)
                    break
                except ValueError:
                    print("\n!!ERROR¡¡ \nSolo puede ingresar numeros enteros")    
        elif opc == 3:
            while True:
                modelo = input("Ingrese el modelo al cual le quiere modificar el precio: ")
                while True:
                    try:
                        p = int(input("Ingrese el nuevo precio: "))
                        actualizar_precio(modelo, p)
                        break
                    except ValueError:
                        print("Solo se permiten numeros enteros")
                denuevo = input("Desea actualizar el precio de otro notebook? (si/no) :").lower()
                if denuevo == "si":
                    continue
                else:
                    break
        elif opc == 4:
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción válida!!")
if __name__ == "__main__":
    main()