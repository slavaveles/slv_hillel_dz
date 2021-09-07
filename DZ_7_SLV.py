# Задача одна, але включає в себе все:
# Вхідні дані: Є файл що містить дані про користувачів, такі як username, id, firstname, lastname розділені
# між собою знаком ; . Тобто: admin;100;Ivan;Ivanov. amin - це username, 100 - це ID і так далі. Приклад файла прикріплений.
#
# Написати функцію що зчитує з файла дані і записує дані в список словників наступного вигляду
#  [ {
#       "username": "admin",
#       "id": 100,
#       "firs_name": "Ivan",
#       "last_name": "Ivanov"
# }, ...],
#
# ID потрібно перетворити в int. Якщо не можна зчитати строку ( id не перетворюється в int ) то записати рядок
# в окремий список. ( Тут потрібно використати конструкцію try). А потім цей список записати
# в окремий файл з назвою wrong_rows.txt
print()
print('CREATE LIST OF DICTIONARIES OUT OF FILE (FUNCTION)')
def file2list(x):
    d = {"username": "admin",
          "id": 100,
          "first_name": "Ivan",
          "last_name": "Ivanov"}
    main = [] # main list of dictionaries with integer IDs
    exceptions = [] # list of exceptions with string IDs
    f = open(x, 'r')
    for line in f.readlines():
          line = line.strip('\n')
          line = list(line.split(';'))
          try:
                isinstance(int(line[1]), int)
                d.update({"username": line[0],
                           "id": int(line[1]),
                           "first_name": line[2],
                           "last_name": line[3]
                           })
                main.append(d.copy())
          except ValueError:
                d.update({"username": line[0],
                           "id": line[1],
                           "first_name": line[2],
                           "last_name": line[3]
                           })
                exceptions.append(d.copy())

    g = open('wrong_rows.txt', 'w')
    g.write(str(exceptions))
    g.close()
    print(f'input file: {x}')
    print()
    print(f'main = {main}')
    print(f'exceptions = {exceptions}')
    f.close()
    print()
    return ('DONE')
print(file2list('users'))


