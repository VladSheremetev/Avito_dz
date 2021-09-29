import csv

DEPARTMENT_NAME = 0
SALARY = 1

menu_options = 'Выберете одну из четырёх команд: \n \
        1 Вывести в понятном виде иерархию команд \n \
        2 Вывести сводный отчёт по департаментам\n \
        3 Сохранить сводный отчёт по департаментам в виде csv-файла\n \
        4 Выход из меню'


def get_department_and_divisions(employee_data_dict: dict) -> dict:
    """Функция, которая возвращает словарь - департамент и его отделы"""

    hierarchy_command = {name_department: set() for name_department in get_department(employee_data_dict)}
    for name_department, name_divisions in zip(employee_data_dict['Департамент'], employee_data_dict['Отдел']):
        hierarchy_command[name_department].add(name_divisions)
    return hierarchy_command


def get_department(employee_data_dict: dict) -> set:
    """Функция, которая возвращает множество департаментов в компании"""
    return set(employee_data_dict['Департамент'])


def get_department_data(name_department: str, employee_data_dict: dict) -> list:
    """Функция, которая возвращает данные для департаменту по окладу"""
    
    return list(filter(lambda x: x[DEPARTMENT_NAME] == name_department, 
                       zip(employee_data_dict['Департамент'], 
                           employee_data_dict['Оклад'])))


def department_summary(name_department: str, department_data: list) -> list:
    """Функция, которая возвращает сводные данные для департамента"""
    
    min_salary_department = min(map(lambda x: float(x[SALARY]), department_data))
    max_salary_department = max(map(lambda x: float(x[SALARY]), department_data))
    sum_salary_department = sum(map(lambda x: float(x[SALARY]), department_data))
    mean_salary_department = str(round(sum_salary_department / len(department_data), 2))
    
    return [name_department, str(len(department_data)), 
            f"{min_salary_department}-{max_salary_department}",
            mean_salary_department]
                                         

def get_summary_data(employee_data_dict: dict) -> dict:
    """Функция, которая возвращает сводные данные для всех департаментов"""
    
    column_headers_summary_data = ['Название', 'Численность', '"Вилка" зарплат', 'Cредняя зарплата']
    dict_summary_data = {headers_summary_data: [] for headers_summary_data in column_headers_summary_data}
    for name_department in get_department(employee_data_dict):
        department_data = get_department_data(name_department, employee_data_dict)
        for headers_column, data_table in zip(column_headers_summary_data, department_summary(name_department, department_data)): 
            dict_summary_data[headers_column].append(data_table)

    return dict_summary_data


def read_file_csv(name_file: str) -> dict:
    """Функция, которая считывает данные из файла"""
    
    with open(name_file, encoding='UTF-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        header = next(reader)
        employee_data_dict = {header_column: [] for header_column in header}
        for line in reader:
            for header_column in header:
                employee_data_dict[header_column].append(line[header_column])
        return employee_data_dict


def print_department_and_divisions(employee_data_dict: dict):
    """Функция, которая печатает в консоль иерархию команд"""
    
    print("Департамент", "|", "Отделы")
    dict_department_and_divisions = get_department_and_divisions(employee_data_dict)
    for department, divisions in dict_department_and_divisions.items():
        print(department + ': ' + ', '.join(divisions))
    print()
    return None


def print_summary_data(dict_summary_data: dict):
    """Функция, которая печатает в консоль сводные данные по департаментам"""
    
    header_columns = dict_summary_data.keys()
    print("{:^17} | {:^17} | {:^17} | {:^17}".format(*header_columns))
    for line_summary_data in zip(dict_summary_data['Название'],
                                 dict_summary_data['Численность'],
                                 dict_summary_data['"Вилка" зарплат'],
                                 dict_summary_data['Cредняя зарплата'],
                                ):
        print("{:^17} | {:^17} | {:^17} | {:^17}".format(*line_summary_data))
    print()
    return None


def print_summary_data_to_csv_file(dict_summary_data: dict):
    """Функция, которая печатает в файл сводные данные по департаментам"""
    
    with open("consolidated_report.csv", 'w', encoding='utf-8') as file:
        header_columns = dict_summary_data.keys()
        file.write(";".join(header_columns) + '\n')
        for line_summary_data in zip(dict_summary_data['Название'],
                                     dict_summary_data['Численность'],
                                     dict_summary_data['"Вилка" зарплат'],
                                     dict_summary_data['Cредняя зарплата'],
                                    ):
            file.write(";".join(line_summary_data) + '\n')
        print("Summary data printed to consolidated_report.csv")
    print()
    return None


def get_command(employee_data_dict: dict):
    
    command = 0
    dict_summary_data = {}
    
    while command != 4:
        print(menu_options)
        command = int(input())
        print()
        if command == 1:
            print_department_and_divisions(employee_data_dict)
        if command == 2:
            if not dict_summary_data:
                dict_summary_data = get_summary_data(employee_data_dict)
            print_summary_data(dict_summary_data)   
        if command == 3: 
            if not dict_summary_data:
                dict_summary_data = get_summary_data(employee_data_dict)
            print_summary_data_to_csv_file(dict_summary_data)
    return None

    
def main():   
    employee_data_dict = read_file_csv("Corp_Summary.csv")
    get_command(employee_data_dict)
    return 1


if __name__ == '__main__':
    main()
