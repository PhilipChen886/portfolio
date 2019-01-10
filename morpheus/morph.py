import sys
import io
from openpyxl import load_workbook

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

origin = ""

def import_text(path):
    wb = load_workbook(path)
    sheet = wb['Sheet1']
    global origin
    origin = sheet.cell(row=1, column=1).value
    return

def print_origin():
    print(origin)
    return

def parse():                                                # hierachy: paragraph >> sentence >> sub-sentence >> elements
    global main_list
    main_list = origin.splitlines()                         # removes newlines
    for i in range (len (main_list)-1, -1, -1):             # removes blank elements
        if (main_list[i] == ''):
            main_list.pop(i)
            i = i+1
    return

def print_main():
    for i in range (len (main_list) ):
        print(main_list[i])
    return

def print_main_list():
    print(main_list)
    return