import json
import os
from datetime import datetime

# Archivo local para ventas
VENTAS_FILE = "ventas.json"

# Menú de productos
menu = {
    "1": {"nombre": "Café", "precio": 2000},
    "2": {"nombre": "Sandwich", "precio": 5000},
    "3": {"nombre": "Jugo", "precio": 3000},
    "4": {"nombre": "Galleta", "precio": 1500}
}

# Cargar historial de ventas
def cargar_ventas():
    if os.path.exists(VENTAS_FILE):
        with open(VENTAS_FILE, "r") as f:
            return json.load(f)
    return []

# Guardar ventas
def guardar_ventas(ventas):
    with open(VENTAS_FILE, "w") as f:
        json.dump(ventas, f, indent=4)

def mostrar_menu():
    print("\n--- MENÚ CAFETERÍA CAMPUS ---")
    for k, v in menu.items():
        print(f"{k}. {v['nombre']} - ${v['precio']}")
    print("0. Finalizar pedido")

def registrar_pedido():
    pedido = []
    total = 0

    while True:
        mostrar_menu()
        opcion = input("Seleccione un producto (0 para terminar): ")
        if opcion == "0":
            break
        if opcion in menu:
            pedido.append(menu[opcion])
            total += menu[opcion]["precio"]
            print(f"Agregado: {menu[opcion]['nombre']} (${menu[opcion]['precio']})")
        else:
            print("Opción inválida.")

    if not pedido:
        print("Pedido vacío.")
        return None

    es_estudiante = input("¿Es estudiante con carné válido? (s/n): ").lower() == "s"
    if es_estudiante:
        total *= 0.9
        print("Descuento aplicado (10% estudiante).")

    # Resumen del pedido
    print("\n--- RESUMEN DEL PEDIDO ---")
    for item in pedido:
        print(f"- {item['nombre']} - ${item['precio']}")
    print(f"TOTAL: ${int(total)}")

    # Guardar en ventas
    ventas = cargar_ventas()
    ventas.append({
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "pedido": [p["nombre"] for p in pedido],
        "total": total
    })
    guardar_ventas(ventas)
    print("✅ Pedido registrado.")

def main():
    print("=== SISTEMA CAFETERÍA CAMPUS ===")
    registrar_pedido()

if __name__ == "__main__":
    main()