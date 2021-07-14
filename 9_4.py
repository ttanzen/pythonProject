
ignore = ["duplex", "alias", "configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status


def convert_config_to_dict (config_filename, **kwargs):
    result = {}

    with  open (config_filename) as f:

        for line in f:
           line = line.rstrip()
           if line and not ignore_command(line, ignore) and line[0] != '!':
               if not line.startswith(' '):
                   dict_key = line.strip()
                   result[dict_key] = []
               elif line.startswith(' '):
                   result[dict_key].append(line.strip())
               else:
                  continue
        return result
print (convert_config_to_dict('config_sw1.txt'))