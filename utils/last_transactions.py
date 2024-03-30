import json
import colorama
from datetime import datetime
from colorama import Fore
from colorama import Back
from colorama import Style


def check_data(data: list):
    """
    Проверяет список словарей на корректность данных
    :param data: список словарей
    :return: True в случе если словари в списке записаны в соответствующем формате
             False в случае если какой-то из требуемых для дальнейшей работы ключей отсутствует
    """
    if len(data) == 0:
        return False
    for i in data:
        if 'id' not in i:
            return False
        elif 'state' not in i:
            return False
        elif 'date' not in i:
            return False
        elif 'operationAmount' not in i:
            return False
        elif 'description' not in i:
            return False
        elif 'to' not in i and 'from' not in i:
            return False
    return True


def prepare_data(dir_to_file: str, stage: int):
    """
    Подготавливает данные к работе. Убирает пустые значения,
    и возвращает требуемое количество отсортированных по дате и времени удачно выполненных операций
    :param dir_to_file: путь к файлу .json в котором хранится история операций
    :param stage: количество данных для загрузки
    :return: если файл получилось считать вернёт список словарей с заданным
    количеством данных, в противном случае возвращает пустой список
    """
    all_operations = []
    if not (".json" in dir_to_file):
        print("Не верный формат файла")
        return all_operations
    with open(dir_to_file, 'r', encoding='utf-8') as file:
        all_operations = json.load(file)
    for i in all_operations:
        if not i:
            all_operations.remove(i)
            continue
    if not check_data(all_operations):
        print("Не верный формат данных")
        return []



    all_operations = sorted(all_operations, key=lambda item: (
        item["state"], datetime.strptime(item["date"][0:19], "%Y-%m-%dT%H:%M:%S")), reverse=True)

    result = []
    for i in range(stage):
        result.append(all_operations[i])

    return result


def hide_data(data: list):
    """
    Скрывает данные о карте или счёте путём форматирования данных в списке словарей
    :param data: список в котором требуется скрыть данные
    :return: если формат хранения данных соответствует требованиям, то будет возращён тот же список, со скрытыми данными
             если формат не соответствует требованиям, то будет возвращён пустой массив
    """
    if not(check_data(data)):
        print("Не верный формат данных")
        return []

    for i in data:
        if 'from' in i:
            if 'Счет' in i['to']:
                i['to'] = i['to'][:5] + '**' + i['to'][-4:]
            else:
                cart = i['to'].split()
                number = cart[len(cart) - 1]
                cart[len(cart) - 1] = ' ' + number[:4] + ' ' + number[5:7] + '** **** ' + number[-4:]
            if 'Счет' in i['from']:
                i['from'] = i['from'][:5] + '**' + i['from'][-4:]
            else:
                cart = i['from'].split()
                number = cart[len(cart) - 1]
                cart[len(cart) - 1] = ' ' + number[:4] + ' ' + number[5:7] + '** **** ' + number[-4:]
                i['from'] = ''.join(cart)
        else:
            if 'Счет' in i['to']:
                i['to'] = i['to'][:5] + '**' + i['to'][-4:]
            else:
                cart = i['to'].split()
                number = cart[len(cart) - 1]
                cart[len(cart) - 1] = ' ' + number[:4] + ' ' + number[5:7] + '** **** ' + number[-4:]

    return data


def print_message(data: dict):
    """
    Вывод форматированного сообщение об одной операции
    :param data: данные об операции
    """
    data['date'] = datetime.strptime(data["date"][0:10], "%Y-%m-%d").strftime("%Y.%m.%d")
    print(Back.LIGHTWHITE_EX + Style.BRIGHT + Fore.BLACK + str(data['date']) + " " + data["description"])
    if 'from' in data:
        print(Fore.LIGHTGREEN_EX + data['from'] + Fore.BLACK + " -> " + Fore.RED + data['to'] + Fore.RESET)
    else:
        print(Fore.LIGHTGREEN_EX + data['to'] + Fore.RESET)
    print(Fore.RED + data['operationAmount']['amount'] + Fore.RESET +
          " " + Fore.BLACK + data['operationAmount']['currency']['name'])
    print(Fore.RESET + Back.RESET)


def last_transactions(dir_to_history: str, stage: int = 5):
    """
    Выводит информацию об указанном количестве последних операциях пользователя
    :param dir_to_history: путь к файлу с историей об операциях пользователя
    :param stage: сколько последних операций требуется вывести
    """
    data = prepare_data(dir_to_history, stage)
    data = hide_data(data)
    for i in data:
        print_message(i)
