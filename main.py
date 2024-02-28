import pickle


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("El producto con el ID especificado no existe en el inventario.")

    def actualizar_producto(self, id, atributo, valor):
        if id in self.productos:
            if atributo == 'cantidad':
                self.productos[id].cantidad = valor
            elif atributo == 'precio':
                self.productos[id].precio = valor
            else:
                print("El atributo especificado no es válido.")
        else:
            print("El producto con el ID especificado no existe en el inventario.")

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.productos.values():
            if producto.nombre == nombre:
                print(producto)
                return
        print("Producto no encontrado.")

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'rb') as f:
                self.productos = pickle.load(f)
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("El archivo especificado no existe.")
        except Exception as e:
            print(f"Ocurrió un error al cargar el inventario: {e}")


def menu():
    print("\n1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario en archivo")
    print("7. Cargar inventario desde archivo")
    print("8. Salir")


def main():
    inventario = Inventario()
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            try:
                id = input("Ingrese ID del producto: ")
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad del producto: "))
                precio = float(input("Ingrese precio del producto: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Por favor, ingrese un valor válido para cantidad y precio.")
        elif opcion == '2':
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = input("Ingrese ID del producto a actualizar: ")
            atributo = input("Ingrese atributo a actualizar (cantidad o precio): ")
            valor = input("Ingrese el nuevo valor: ")
            inventario.actualizar_producto(id, atributo, valor)
        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)
        elif opcion == '5':
            inventario.mostrar_productos()
        elif opcion == '6':
            archivo = input("Ingrese el nombre del archivo para guardar el inventario: ")
            inventario.guardar_inventario(archivo)
            print("Inventario guardado correctamente.")
        elif opcion == '7':
            archivo = input("Ingrese el nombre del archivo para cargar el inventario: ")
            inventario.cargar_inventario(archivo)
        elif opcion == '8':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()