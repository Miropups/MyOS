import flet as ft
import os

version  = 0.4
print(f"VERSION {version} now is running")
def main(page: ft.Page):

    def take_command(e):
        print(f"ввод комманды - {user_text.value}")
        lastComands.controls.append(ft.Text(f"MAX OS: {command_process(user_text.value)}"))
        user_text.value = ''
        user_text.focus()
        page.update()
    def command_process(command_text: str):
        command_text = command_text.split()
        match command_text[0]:
            case "cd":
                return " ".join(command_text)
            case "ls":
                return " ".join(command_text)
            case "echo":
                return os.getenv(command_text[1])
            case "exit":
                page.window.close()
                return "выключение программы"
            case _:
                return f"{command_text[0]} // INCORRECTED COMMAND"
              
    user_per_text = "MAX OS: "
    console_text = ft.Text(user_per_text)
    user_text = ft.TextField(width=200, on_submit=take_command, border='None', autofocus=True)

    page.title = "VFS"
    page.theme_mode ='dark'
    page.vertical_alignment = ft.MainAxisAlignment.START   

    lastComands = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    page.add(
        lastComands,
        ft.Row(
            [
                console_text,
                user_text
            ],
            alignment=ft.MainAxisAlignment.START
        )
    )


ft.app(target=main) #указываешь функцию, где прописываешь страничку
