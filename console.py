import sys

#матрица комманд
file_name = ''
VFX_path = ''

def correct_input():

    parametrs = sys.argv
    if len(parametrs)>2:
        print("есть параметры")

        global file_name
        global VFX_path

        VFX_path = parametrs[1]
        file_name = parametrs[2]
        
        try:
            open(file_name, mode = 'r')
            return "файл успешно загружен"
        except:
            return "неверный путь к файлу загрузки комманд"
    
    else:
        print("нет параметров")
        return "параметы не были введены"

def get_command_list():
    commandList = []
    global file_name
    
    with open(file_name, mode = 'r') as file:
        for line in file:
            #print(line.split())
            command =[]
            for element in line.split():
                #тут мы получаем elemnt - комманда
                
                if element[0] == "#" or element == "#": #определяет комментарий, если он, то дальше его не считывает
                    print("!!!комментарий дальше")
                    break
                command.append(element)
            commandList.append(command)
            print("-------------------------- след строчка")
    return commandList
    
            
print("код выполнен")




    

