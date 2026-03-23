import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro App Flet"
    page.bgcolor = "blue"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text("Olá Mundo!!", size=24),
        ft.Text("Aqui você pode criar o que quiser!", size=24)
    )

ft.run(main)