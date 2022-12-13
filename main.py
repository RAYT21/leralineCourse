import os
import socket
from tkinter import *
from tkinter.filedialog import asksaveasfile
import re
import time

class Window:

    def __init__(self):
        self.result_output = None
        self.root = Tk()
        self.root.title('Программа проверки информационной безопасности')
        self.root.geometry('1000x600')
        self.root.resizable(True, True)

        self.internet = Button(self.root, command=self.internet_connection_click,
                               text='Проверка наличия соединения  \nс интернетом', width=35, bg="#b38dd9", font='Consolas')
        self.internet.place(x=20, y=10)
        self.internet_result = Label(self.root, text='Проверка не проводилась', font='Consolas')
        self.internet_result.place(x=400, y=10)

        self.firewall_place = Button(self.root, command=self.firewall_install_click,
                                     text='Проверка наличия установленного \nмежсетевого экрана', width=35, bg="#b38dd9", font='Consolas')
        self.firewall_place.place(x=20, y=70)
        self.firewall_place_result = Label(self.root, text='Проверка не проводилась', font='Consolas')
        self.firewall_place_result.place(x=400, y=70)

        self.firewall_status = Button(self.root, command=self.firewall_work_click,
                                      text='Проверка работоспособности \nмежсетевого экрана', width=35, bg="#b38dd9", font='Consolas')
        self.firewall_status.place(x=20, y=130)
        self.firewall_status_result = Label(self.root, text='Проверка не проводилась', font='Consolas')
        self.firewall_status_result.place(x=400, y=130)

        self.antivirus_place = Button(self.root, command=self.antivirus_install_click,
                                      text='Проверка наличия \nустановленного антивирусного ПО', width=35, bg="#b38dd9", font='Consolas')
        self.antivirus_place.place(x=20, y=190)
        self.antivirus_place_result = Label(self.root, text='Проверка не проводилась', font='Consolas')
        self.antivirus_place_result.place(x=400, y=190)

        self.antivirus_status = Button(self.root, command=self.antivirus_work_click,
                                       text='Проверка работоспособности \nантивирусного ПО', width=35, bg="#b38dd9", font='Consolas')
        self.antivirus_status.place(x=20, y=250)
        self.antivirus_status_result = Label(self.root, text='Проверка не проводилась', font='Consolas')
        self.antivirus_status_result.place(x=400, y=250)

        self.result_painting = Button(self.root, command=self.result_painting_click, text='Вывести результат', bg="#4169e1",
                                      font='Consolas')
        self.result_painting.place(x=20, y=330)
        self.result_painting_result = Listbox(self.root, width=55, bd=10, font='Consolas')
        self.result_painting_result.place(x=400, y=330)

        self.result_file = Button(self.root, command=self.result_file_click, text='Вывести результат в файл', bg="#4169e1",
                                  font='Consolas')
        self.result_file.place(x=20, y=380)

        self.exit = Button(self.root, command=self.exit_click, text='Выйти', bg="red", font='Consolas')
        self.exit.place(x=20, y=520)

        self.root.mainloop()

    def internet_connection_click(self):
        try:
            sock = socket.create_connection(("www.google.com", 80))
            if sock is not None:
                sock.close()
            self.internet_result.config(text='Данный компьютер подключен к интернету', fg='green')
            return
        except OSError:
            pass
        self.internet_result.config(text='Данный компьютер не подключен к интернету', fg='red')

    def firewall_install_click(self):
        lst = os.popen('firewall-cmd --version').read()
        lst = lst.split('\n')
        flag = False
        for i in range(0, len(lst)):
            if (re.search(r'\d.\d.\d',lst[i])):
                flag = True
                break
        if (flag):
            self.firewall_place_result.config(text='Межсетевой экран Firewalld установлен', fg='green')
        else:
            self.firewall_place_result.config(text='Межсетевой экран Firewalld не установлен', fg='red')

    def firewall_work_click(self):
        #добавляем правило на блокировку доступа к сайту
        os.popen('firewall-cmd --add-rich-rule="rule family=\'ipv4\' source address=\'172.217.17.238\' reject"; firewall-cmd --reload')
        # пингуем его
        time.sleep(10)
        flag = False
        try:
            sock = socket.create_connection(("www.google.com", 80))
            if sock is not None:
                sock.close()
            flag = True
        except OSError:
            pass
        # убираем настройку
        os.popen('firewall-cmd --remove-rich-rule="rule family=\'ipv4\' source address=\'172.217.17.238\' reject"; firewall-cmd --reload')
        time.sleep(4)
        if (flag):
            self.firewall_status_result.config(text='Межсетевой экран Firewalld функционирует', fg='green')
        else:
            self.firewall_status_result.config(
                text='Межсетевой экран функционирует неверно, или не функционирует вовсе', fg='red')

    def antivirus_install_click(self):
        lst = os.popen('drweb-ctl -v').read()
        lst = lst.split('\n')
        flag = False
        for i in range(0, len(lst)):
            if (lst[i] == 'drweb-ctl 11.1.9.2103151924'):
                flag = True
                break
        if (flag):
            self.antivirus_place_result.config(text='Антивирус DrWeb установлен', fg='green')
        else:
            self.antivirus_place_result.config(text='Антивирус DrWeb не установлен', fg='red')

    def antivirus_work_click(self):
        lst = os.popen('ps -aux | grep [d]rweb').read()
        lst = lst.split('\n')
        flag = False
        for i in range(0, len(lst)):
            if (lst[i].__contains__('drweb-spider')):
                flag = True
                break
        if (flag):
            self.antivirus_status_result.config(text='Монитор DrWeb функционирует', fg='green')
        else:
            self.antivirus_status_result.config(
                text='Монитор DrWeb не функционирует, или функционирует неправильно', fg='red')

    def result_painting_click(self):
        self.result_output = ''
        self.result_output = 'Результаты проведенного тестирования:\n'
        # internet
        if (self.internet_result['text'] == 'Проверка не проводилась'):
            self.result_output += "1. Тестирование подключения к интернету не проводилось\n"
        else:
            if (self.internet_result['text'] == 'Данный компьютер подключен к интернету'):
                self.result_output += "1. Данный компьютер подключен к интернету\n"
            else:
                self.result_output += "1. Данный компьютер не подключен к интернету\n"
        # firewall

        if (self.firewall_place_result['text'] == 'Проверка не проводилась'):
            self.result_output += "2. Тестирование межсетевого экрана не проводилось\n"
        else:
            if (self.firewall_place_result['text'] == 'Межсетевой экран DrWeb установлен!'):
                self.result_output += "2. Межсетевой экран DrWeb установлен, "
                if (self.firewall_status_result['text'] == 'Тестирование не проводилось'):
                    self.result_output += "но тестирование его работоспособности не проводилось\n"
                else:
                    if (self.firewall_status_result['text'] == 'Межсетевой экран DrWeb функционирует'):
                        self.result_output += "верно функционирует\n"
                    else:
                        self.result_output += "неверно или вообще не фукционирует\n"
            else:
                self.result_output += "2. Межсетевой экран DrWeb не установлен\n"

        # antivirus(скопировать фаервольный вывод, просто поменять поля (конечно же после того, как поправить  выводы))
        if (self.antivirus_place_result['text'] == 'Проверка не проводилась'):
            self.result_output += "3. Тестирование антивирусного ПО не проводилось\n"
        else:
            if (self.antivirus_place_result['text'] == 'Антивирус DrWeb установлен'):
                self.result_output += "3. Антивирус DrWeb установлен, "
                if (self.antivirus_status_result['text'] == 'Тестирование не проводилось'):
                    self.result_output += "но тестирование работоспособности монитора не проводилось\n"
                else:
                    if (self.antivirus_status_result['text'] == 'Монитор DrWeb функционирует'):
                        self.result_output += "монитор верно функционирует\n"
                    else:
                        self.result_output += "но монитор функционирует неверно, или вообще не фукционирует\n"
            else:
                self.result_output += "3. Антивирус DrWeb не установлен\n"

        self.internet_result.config(text='Проверка не проводилась', fg='black')
        self.firewall_status_result.config(text='Проверка не проводилась', fg='black')
        self.firewall_place_result.config(text='Проверка не проводилась', fg='black')
        self.antivirus_status_result.config(text='Проверка не проводилась', fg='black')
        self.antivirus_place_result.config(text='Проверка не проводилась', fg='black')
        self.result_painting_result.delete(0, END)
        print(self.result_output)
        list = self.result_output.split('\n')
        for i in list:
            self.result_painting_result.insert(END, i)


    def result_file_click(self):
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        text2save = str(self.result_output)
        f.write(text2save)
        f.close()

    def exit_click(self):
        self.root.destroy()


wind = Window()
