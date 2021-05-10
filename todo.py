import time


HELP = """
help - помощь
add  - добавить
show  - показать
done   - убрать
exit    - выкл
"""


todo = {} 

def checkDate(date):
  try:
    time.strptime(date, "%d.%m.%Y")
    return True
  except ValueError:
    print("Error")
    return False 

def add(command, userAnswer):
  if userUnswer == "add":
    userDate = input("Введите дату:\n")
    if checkDate (userDate) == False:
      continue 
    userTask = input("Что нужно сделать?")

    if userDate in todo.keys():
      todo[ userDate ].append( userTask )
    else:
      todo[ userDate ] = ( userTask )
    todo[ userDate] = userTask
    print(f" [ {userDate} ] - добавленная задача '{userTask}' ")

print("Введите команду или help, для вывода доступных команд")

while True:
  userUnswer = input()

  
  elif userUnswer == "help":
    print(HELP) 
  elif userUnswer == "show":
    for date in sorted( todo.keys() ):
      for tasks in todo[ date ]:
        print( f"[{date}] - {tasks}" ) 
  elif userUnswer == "exit":
    break 
  elif userUnswer == "help":
    print("Работает") 
