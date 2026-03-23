import flet as ft


def main(page: ft.Page):
    page.title = "Teste botões",
    page.add(
        ft.Text("Bem-Vindo ao meu app!", size=20),
        ft.Text("Este é um texto menor", size=16, color="blue"),
    )

    def botao_clicado(e):
        page.add(
            ft.Text("Voce clicou no Botão!", color="red", size=25)
        )

    def botao_numeros(e: ft.Event[ft.Button]):
        button.data += 1
        message.value = f"Botao colorido clicado {button.data} vezes"
        page.update()

    page.add(
        ft.Button(
            content="Clique Aqui!",
            on_click=botao_clicado
        ),
        button := ft.Button(
            content=f"Botao Colorido com cliques",
            data=0,
            on_click=botao_numeros,
            bgcolor="blue", color="white"
        ),
        message := ft.Text(),
        ft.Button(
            content="Botao Desativado",
            disabled=True,
            on_click=botao_clicado
        ),
        ft.Button(
            content="Botao Com Icone",
            icon=ft.Icons.SAVE,
            icon_color=ft.Colors.BLUE_600
        )
    ),
    page.add(
        ft.Image(
            src="https://www.sp.senai.br/images/senai.svg",
            width=150,
            height=150
        )
    )


ft.run(main)
