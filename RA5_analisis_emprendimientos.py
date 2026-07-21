"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_total(ventas):
    """Recibe una lista y retorna el total de ventas."""
    return sum(ventas)

def calcular_porcentaje_logro(total, meta):
    """Recibe una lista de ventas y un valor meta. Retorna el porcentaje de logro."""
    porcentaje = total / meta * 100
    return porcentaje

def calcular_clasificacion (porcentaje):
    if porcentaje >= 100:
        mensaje = "Meta alcanzada; felicidades..!"
    elif porcentaje >= 90:
        mensaje = "Advertencia, Meta no lograda"
    else:
        mensaje = "Urgente!! Meta no lograda"
    return mensaje

def imprimir_reporte(datos_reporte):
    """Imprime el reporte final de ventas por emprendimiento"""
    print("\nReporte final")
    print("_" * 60)
    
    for fila in datos_reporte:
        print(f"sede: {fila["nombre"]}")
        print(f"provincia: {fila["provincia"]}")
        print(f"tipo: {fila["tipo"]}")
        
        print(f"Total de ventas semanal: ₵{fila["total"]:,.2f}")
        print(f"Porcentaje meta: {fila["porcentaje"]:.2f}%")
        print(f"Promedio diario: {fila["total"]/5:,.2f}")
        print(fila["clasificacion"])
        
        print("_" * 60)



print("La variable sedes es tipo", type(sedes).__name__)

reporte = []
for emprendimiento in sedes:
#primer_emprendimiento = sedes[0]
#print("Primer emprendimiento: ", primer_emprendimiento)
#print("Tipo:", type(primer_emprendimiento).__name__)
#print("Nombre: " , primer_emprendimiento["nombre"])
#print("Provincia: ", primer_emprendimiento["provincia"])
#print("Ventas: ", primer_emprendimiento["ventas"])
    ventas = emprendimiento["ventas"]
    meta = emprendimiento["meta"]
    nombre = emprendimiento["nombre"]

    total_ventas = calcular_total(ventas)
    porcentaje_emprendimiento=calcular_porcentaje_logro(total_ventas,meta)
    clasificacion = calcular_clasificacion(porcentaje_emprendimiento)
    
    reporte.append(
        {
            "nombre" : emprendimiento["nombre"],
            "provincia" : emprendimiento["provincia"],
            "tipo" : emprendimiento["tipo"],
            "total" : total_ventas,
            "clasificacion" : clasificacion,
            "porcentaje" : porcentaje_emprendimiento,
        }
    )

imprimir_reporte(reporte)