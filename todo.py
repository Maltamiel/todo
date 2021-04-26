HELP = """
help - помощь
add  - добавить
show  - показать
done   - убрать
exit    - выкл
"""

todo = {} 
print("Введите команду или help, для вывода доступных команд")

while True:
  userUnswer = input()

  if userUnswer == "add":
    userDate = input("Введите дату:\n")
    userTask = input("Что нужно сделать?")

    if userDate in todo.keys():
      todo[ userDate ].append( userTask )
    else:
      todo[ userDate ] = ( userTask )
    todo[ userDate] = userTask
    print(f" [ {userDate} ] - добавленная задача '{userTask}' ")
  elif userUnswer == "help":
    print(HELP) 
  elif userUnswer == "show":
    print("Работает") 
  elif userUnswer == "exit":
    break 
  elif userUnswer == "help":
    print("Работает") 
