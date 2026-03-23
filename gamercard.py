import flet as ft


def main(page: ft.Page):
    # Configurações da Janela
    page.title = "Gamer Card"
    page.bgcolor = "1E1E1E"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Cabeçalho: Avatar (Emoji) e Nome do Lado
    cabecalho = ft.Row(
        controls=[
            ft.Text("🥷", size=60),  # Emoji a prova de erros
            ft.Column(
                controls=[
                    ft.Text("SHADOW_NINJA", size=24,
                            weight="bold", color="white"),
                    ft.Text("Nível 42 - Ninja das Sombras",
                            size=24, color="grey300")
                ], spacing=2
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Status: Barra de HP, MP e XP


ft.run(main)
