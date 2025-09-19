import flet as ft
import os
import console


version  = 0.5
print(f"VERSION {version} now is running")







def main(page: ft.Page):
    
    def showTextOnScreen(textForScreen:str): #функция вывода текста на экран
        lastComands.controls.append(ft.Text(f"MAX OS: {textForScreen}"))
        user_text.value = ''
        user_text.focus()
        page.update()

    def take_command(e): #функция, которая выполняется при нажатии ввода
        inputed_text = e.data
        print(f"ввод комманды - {inputed_text}")
        showTextOnScreen(command_process(inputed_text.split()))
        

        
    def command_process(command_text): #функция которая обрабатывает команду, получая список на входе и возвращает тектс
        
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
    showTextOnScreen(console.correct_input()) # выводит результат работы с файлом
    try:
        for command in console.get_command_list(): #command - список
            command_output = command_process(command)
            print(f"ввод комманды через файл - {command_output}")
            showTextOnScreen(command_process(command_output.split()))
    except:
        pass



ft.app(target=main) #указываешь функцию, где прописываешь страничку
