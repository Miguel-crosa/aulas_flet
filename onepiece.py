import flet as ft


def main(page: ft.Page):
    page.title = "One Piece",
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def mostrar_mensagem(e):
        page.add(
            ft.Text(
                "Eu vou ser o rei dos piratas",
                col="red",
                size=18
            )
        ),
    page.add(
        ft.Text(
            "Olá meu nome é Luffy",
            color="purple",
            size=20
        ),
        ft.Image(
            src="images/luffy.jpg",
            height=200
        ),
        ft.Button(
            content="Clique Aqui",
            on_click=mostrar_mensagem
        )
    )


ft.run(main)
