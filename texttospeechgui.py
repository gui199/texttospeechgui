#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:33:07 2022
@author: gui
"""
import PySimpleGUI as sg
import os

sg.theme('DarkBlue4')

cmd = "gtts-cli -l "
cmd3 = "' | play -t mp3 -"
cmd4 = "'   --output "
mp3 = ".mp3"

lang_en = ["com", "co.uk", "ca", "com.au", "co.in", "co.za", "ie"]
lang_pt = ["com.br", "pt"]
lang_es = ["com", "es", "com.mx"]

layout = [
    [sg.Text('Texto para Fala', size=(40, 1), font=('Any 15'))],
    [sg.MLine(default_text='Digite qualquer coisa...', size=(55, 25),
              key='-INPUT-', text_color="red", background_color='white',
              tooltip="Digite qualquer coisa...",)],
    [sg.InputText(size=(45, 1), key='-INAME-', disabled=True),
     sg.FileBrowse(button_text='Abrir Arq.',
                   file_types=(("Arq Texto", "*.txt"),),
                   tooltip="Selecionar Arquivo de Texto",)],
    [sg.Radio('pt', "RADIO1", default=True, size=(4, 1),
              enable_events=True, key="-IN1-"),
     sg.Radio('en', "RADIO1", size=(4, 1), enable_events=True, key="-IN2-"),
     sg.Radio('es', "RADIO1", size=(5, 1),  enable_events=True, key="-IN3-"),
     sg.Text('Sotaque:'),
     sg.Combo(lang_pt, default_value=lang_pt[1],
              key='other_key', size=(15, 0))],
    [sg.Button('Falar do Texto',  button_color=('white', 'firebrick3'),
               key='-PASTE-'),
     sg.OK('Limpar', key='-CLEAR-', button_color=('white', 'red')),
     sg.Button('Falar do Arquivo', button_color=('white', 'firebrick3'),
               key='-FILE-')],
    [sg.Text('Digite o nome do arquivo:', text_color="white", )],
    [sg.Input("arquivo_mp3", key='-FIILENAME-'),
     sg.Button('Salvar',  button_color=('white', 'firebrick3'), key='-SAVE-',
               tooltip="Gravar MP3 do Texto ou Arquivo.",)],
    ]

janela = sg.Window('Text to Speech', layout=layout, auto_size_text=True,
                   alpha_channel=0.1, resizable=True, location=(400, 400),
                   size=(500, 600))


def check_language():
    textlang = valores['other_key']
    if valores["-IN2-"]:
        return "en  -t "+textlang
    elif valores["-IN1-"]:
        return "pt -t "+textlang
    elif valores["-IN3-"]:
        return "es -t "+textlang


# ler os eventos
while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == '-CLEAR-':
        janela['-INPUT-'].update('')
        janela['-INAME-'].update('')
    if eventos == '-PASTE-':
        text = valores['-INPUT-']
        lang = check_language()
        result = cmd+lang+"  '"+text+cmd3
        # sg.popup(result)
        os.system(result)
    if eventos == '-FILE-':
        iname = valores['-INAME-']
        if not iname:
            sg.popup("Nenhum Arq Selecionado")
        else:
            lang = check_language()
            result = cmd+lang+" -f '"+iname+cmd3
            # sg.popup(result)
            os.system(result)
    if eventos == '-SAVE-':
        iname = valores['-INAME-']
        text = valores['-INPUT-']
        fname = valores['-FIILENAME-']
        if not iname:
            lang = check_language()
            result = cmd+lang+" '"+text+cmd4+fname+mp3
            sg.popup("Salvando", title="Salvando",)
            os.system(result)
        else:
            lang = check_language()
            result = cmd+lang+" -f '"+iname+cmd4+fname+mp3
            sg.popup("Salvando")
            os.system(result)
    if valores["-IN2-"]:
        janela['other_key'].update(value=lang_en[0], values=lang_en,)
    elif valores["-IN1-"]:
        janela['other_key'].update(value=lang_pt[1], values=lang_pt,)
    elif valores["-IN3-"]:
        janela['other_key'].update(value=lang_es[2], values=lang_es, )

janela.close()
