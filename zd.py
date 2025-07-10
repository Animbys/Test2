def load_employees(filename):
    employees = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(', ')
                if len(parts) == 3:
                    employees.append(parts)  # [fam, name, age]
    except FileNotFoundError:
        pass
    return employees

def save_employees(filename, employees):
    with open(filename, 'w', encoding='utf-8') as f:
        for emp in employees:
            f.write(', '.join(emp) + '\n')

filename = 'zz.txt'
employees = load_employees(filename)

while True:
    command = input("(Aap, Redact, ydon, exit) ").strip()

    if command == "Aap":
        Fam = input("Фамилия: ").strip()
        Name = input("Имя: ").strip()
        age = input("Возраст: ").strip()
        employees.append([Fam, Name, age])
        save_employees(filename, employees)
        print("Сотрудник добавлен.")

    elif command == "Redact":
        fam_to_edit = input("Введите фамилию сотрудника для редактирования: ").strip()
        found = False
        for i, emp in enumerate(employees):
            if emp[0] == fam_to_edit:
                print(f"Найдена запись: {emp}")
                Fam = input(f"Новая фамилия (Enter чтобы оставить {emp[0]}): ").strip()
                Name = input(f"Новое имя (Enter чтобы оставить {emp[1]}): ").strip()
                age = input(f"Новый возраст (Enter чтобы оставить {emp[2]}): ").strip()
                if Fam:
                    employees[i][0] = Fam
                if Name:
                    employees[i][1] = Name
                if age:
                    employees[i][2] = age
                found = True
                print("Данные обновлены.")
                break
        if not found:
            print("Сотрудник с такой фамилией не найден.")
        save_employees(filename, employees)
    elif command == "ydon":
        fam_to_delete = input("Введите фамилию сотрудника для удаления: ").strip()
        before_count = len(employees)
        employees = [emp for emp in employees if emp[0] != fam_to_delete]
        after_count = len(employees)
        if before_count == after_count:
            print("Сотрудник с такой фамилией не найден.")
        else:
            print(f"Удалено {before_count - after_count} сотрудников.")
            save_employees(filename, employees)

    elif command == 'poisk':
        fam_to_edit = input("Введите фамилию сотрудника для редактирования: ").strip()
        for i, emp in enumerate(employees):
            if emp[0] == fam_to_edit:
                print(f"Найдена запись: {emp}")
            else:
                print("Сотрудник с такой фамилией не найден.")
    elif command == "ospoisk":
        fam_to_edit = input("Введите возраст сотрудника: ").strip()
        for i, emp in enumerate(employees):
            if emp[2] == fam_to_edit:
                print(f"Найдена запись: {emp}")
            else:
                print("Сотрудник с такой фамилией не найден.")


    elif command == "exit":
        print("Выход из программы.")
        break




