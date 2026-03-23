import flet as ft


def main(page: ft.Page):
    page.title = "Row",
    page.bgcolor = "blue"

    page.add(
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("Esquerda"),
                    ft.Button(content="Botão do Meio"),
                    ft.Text("Botão da direita")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=20
            ),
            bgcolor="red",
            height=500,
            width=400
        )
    )


ft.run(main)
