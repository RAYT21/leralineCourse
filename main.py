from tkinter import *
import os
import socket
import fileinput
from tkinter.filedialog import asksaveasfile


class Window:

    def __init__(self):
        self.root = Tk()
        self.root.title('Программа проверки информационной безопасности')
        self.root.geometry('600x400')
        self.root.resizable(True, True)

        self.internet = Button(self.root, command=self.internet_connection_click,
                               text='Проверка наличия соединения с интернетом', font='Consolas')
        self.internet.place(x=20, y=10)
        self.internet_result = Label(self.root, text='Проверка не проводилась', font='Consolas')
        self.internet_result.place(x=500, y=10)

        self.firewall_place = Button(self.root, command=self.firewall_install_click,
                                     text='Проверка наличия установленного межсетевого экрана', font='Consolas')
        self.firewall_place.place(x=20, y=50)
        self.firewall_place_result = Label(self.root, text='Проверка не проводилась', font='Consolas')
        self.firewall_place_result.place(x=500, y=50)

        self.firewall_status = Button(self.root, command=self.firewall_work_click,
                                      text='Проверка работоспособности межсетевого экрана', font='Consolas')
        self.firewall_status.place(x=20, y=90)
        self.firewall_status_result = Label(self.root, text='Проверка не проводилась', font='Consolas')
        self.firewall_status_result.place(x=500, y=90)

        self.antivirus_place = Button(self.root, command=self.antivirus_install_click,
                                      text='Проверка наличия установленного антивирусного ПО', font='Consolas')
        self.antivirus_place.place(x=20, y=160)
        self.antivirus_place_result = Label(self.root, text='Проверка не проводилась', font='Consolas')
        self.antivirus_place_result.place(x=500, y=160)

        self.antivirus_status = Button(self.root, command=self.antivirus_work_click,
                                       text='Проверка работоспособности антивирусного ПО', font='Consolas')
        self.antivirus_status.place(x=20, y=200)
        self.antivirus_status_result = Label(self.root, text='Проверка не проводилась', font='Consolas')
        self.antivirus_status_result.place(x=500, y=200)

        self.result_painting = Button(self.root, command=self.result_painting_click, text='Вывести результат',
                                      font='Consolas')
        self.result_painting.place(x=350, y=260)
        self.result_painting_result = Listbox(self.root, font='Consolas')
        self.result_painting_result.place(x=20, y=260)

        self.result_file = Button(self.root, command=self.result_file_click, text='Вывести результат в файл',
                                  font='Consolas')
        self.result_file.place(x=350, y=300)

        self.exit = Button(self.root, command=self.exit_click, text='Выйти', font='Consolas')
        self.exit.place(x=350, y=340)

        self.root.mainloop()


    def internet_connection_click(self):
        print('123')
        try:
            print(231)
            sock = socket.create_connection(("www.google.com", 80))
            if sock is not None:
                print(231)
                sock.close
            print(231)
            self.internet_result.config(text='Данный компьютер подключен к интернету!', fg='green')
            return
        except OSError:
            pass
        self.internet_result.config(text='Данный компьютер не подключен к интернету!', fg='red')

    def firewall_install_click(self):
        lst = os.popen('drweb-ctl -v').read()
        lst = lst.split('\n')
        flag = False
        for i in range(0, len(lst)):
            if (lst[i] == 'drweb-ctl 11.1.9.2103151924'):
                flag = True
                break
        if (flag):
            self.firewall_place_result.config(text='Межсетевой экран DrWeb установлен!', fg='green')
        else:
            self.firewall_place_result.config(text='Межсетевой экран DrWeb не установлен!', fg='red')

    def firewall_work_click(self):
        lst = os.popen('ps -aux | grep [d]rweb').read()
        lst = lst.split('\n')
        flag = False
        for i in range(0, len(lst)):
            if (lst[i].__contains__('drweb-firewall')):
                flag = True
                break
        if (flag):
            self.firewall_status_result.config(text='Межсетевой экран DrWeb функционирует!', fg='green')
        else:
            self.firewall_status_result.config(text='Межсетевой экран функционирует неверно, или не функционирует вовсе!', fg='red')

    def antivirus_install_click(self):
        lst = os.popen('drweb-ctl -v').read()
        lst = lst.split('\n')
        flag = False
        for i in range(0, len(lst)):
            if (lst[i] == 'drweb-ctl 11.1.9.2103151924'):
                flag = True
                break
        if (flag):
            self.antivirus_place_result.config(text='Антивирус DrWeb установлен!', fg='green')
        else:
            self.antivirus_place_result.config(text='Антивирус DrWeb не установлен!', fg='red')

    def antivirus_work_click(self):
        lst = os.popen('ps -aux | grep [d]rweb').read()
        lst = lst.split('\n')
        flag = False
        for i in range(0, len(lst)):
            if (lst[i].__contains__('drweb-spider')):
                flag = True
                break
        if (flag):
            self.antivirus_status_result.config(text='Антивирус DrWeb функционирует!', fg='green')
        else:
            self.antivirus_status_result.config(
                text='Антивирус DrWeb не функционирует, или функционирует неправильно!', fg='red')

    def result_painting_click(self):
        self.result_painting_result = 'Результаты проведенного тестирования антивируса и фаервола\n'
        if (self.internet_result != 'Проверка не проводилась'):
            self.result_painting_result += "1. Тестирование интернет соединения не проводилось\n"
        else:
            if (self.internet_result == 'Работает'):
                self.result_painting_result += "1. Тестирование интернет соединения не проводилось\n"
            else:
                self.result_painting_result += "1. Тестирование интернет соединения не проводилось\n"

        if (self.firewall_place_result != 'Проверка не проводилась'):
            self.result_painting_result += "2. Тестирование межсетевого экрана не проводилось\n"
        else:
            if (self.firewall_place_result == 'Работает'):
                self.result_painting_result += "2. Тестирование интернет соединения не проводилось\n"
                if(self.firewall_status_result):
                    self.result_painting_result += "1. Тестирование интернет соединения не проводилось\n"
            else:
                self.result_painting_result += "2. Межсетевой экран не установлен\n"

        if (self.internet_result != 'Проверка не проводилась'):
            self.result_painting_result += "1. Тестирование интернет соединения не проводилось\n"
        else:
            if (self.internet_result == 'Работает'):
                self.result_painting_result += "1. Тестирование интернет соединения не проводилось\n"
            else:
                self.result_painting_result += "1. Тестирование интернет соединения не проводилось\n"




    def result_file_click(self):
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        text2save = str(self.result_painting_result)
        f.write(text2save)
        f.close()

    def exit_click(self):
        self.root.destroy()


wind = Window()
