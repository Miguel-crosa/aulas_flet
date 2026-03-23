import flet as ft


# HABILITAR O SCROLL DO MOUSE
# def main(page: ft.Page):
#     page.scroll = ft.ScrollMode.AUTO
#     page.title = "Row e Column"
# ROLA A TELA INTEIRA
#     for i in range(100+1):
#         page.add(
#             ft.Text(f"Item: {i}")
#         )
# PARA HABILITAR SOMENTE UMA PARTE DO CÓDIGO, USE:
# page.scroll = ft.ScrollMode.ALWAYS, exemplo:
# page.add(
#   ft.Column(
#       controls=[
# ft.Text(f"Item [i]") for i in range(100+1)
# ], height=300, scroll = ft.ScrollMode.ALWAYS
#   )
# )

def main(page: ft.Page):
    page.add(
        ft.Column(
            [
                ft.Text("Título do App",
                        size=22,
                        weight="bold"
                        ),
                ft.Row(
                    [
                        ft.ElevatedButton(content="Botão 1"),
                        ft.ElevatedButton(content="Botão 2"),
                        ft.ElevatedButton(content="Botão 3"),
                    ], spacing=10
                ),
                ft.Text("Rodapé do App")
            ], spacing=20
        )
    )


ft.run(main)
