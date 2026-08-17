import flet as ft

def main(page: ft.page):
    page.title = "Calculadora"
    page.add(ft.Text("Hola, mundo!"))
    
    ft.run(main)

result = ft. text(value="0", size=20)
button = ft.Container(
    content=ft.Text("7"),
    width=60
    height=60,
    alignment=ft.alignment=.center,
)

page.add(result, button)