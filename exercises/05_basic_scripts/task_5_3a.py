# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
choice ={"access": {"template": access_template, "quiz": "Введите номер VLAN:"}, "trunk": {"template": trunk_template, "quiz": "Введите разрешенные VLANы:"}}
tipe = input("Введите режим работы интерфейса (access/trunk):")
number = input("Введите тип и номер интерфейса:")
vlanNumber = input(choice[tipe]["quiz"])
template = choice[tipe]["template"]
result = '''interface {}
{}'''.format(number, '\n'.join(template).format(vlanNumber))
print(result)


