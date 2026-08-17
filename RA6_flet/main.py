import flet as ft


def main(page: ft.page):
    page.tittle = "Mi primer app con Flet"
    mensaje = ft.Text("Aqui va un mensaje")
    nombre = ft.TextField(label="escriba su nombre", autofocus=True)
    
    def mostrar_mensaje(txt_mensaje):
        dialogo = ft.AlertDialog(
            title=ft.Text("Mensaje"),
            content=ft.Text(txt_mensaje)
        )
    
    def saludar (e):
        if nombre.value.strip() =="":
            mensaje.value = "Hola desconocido"
        else:
            mensaje.value = "Hola, " + nombre.value
            mostrar_mensaje(mensaje.value)
        
        
    page.add(
        ft.Text("Hola Daniel!!"),
        ft.Button("Click aqui!!", on_click = saludar),
        mensaje,
        nombre
        )
        
ft.run(main)