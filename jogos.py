import flet as ft


def main(page: ft.Page):
    page.title = "Resident Evil Requiem",
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def mostrar_mensagem(e):
        page.add(
            ft.Image(
                src="images/residentevil.jpg",
                height=200
            ),
            ft.Image(
                src="images/crimson.jpg",
                height=200
            ),
            ft.Text(
                "Jogos mais recentes amados pelo povo!",
                color="red",
                size=20
            )
        ),
    page.add(
        ft.Text(
            "Novos lançamentos, jogos mais recentes falados ativamente",
            color="purple",
            size=20
        ),
        ft.Button(
            content="Clique Aqui",
            on_click=mostrar_mensagem
        )
    )


ft.run(main)
