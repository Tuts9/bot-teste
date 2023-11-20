from telebot import types

option_buttons = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
op1 = types.KeyboardButton(text='/Começar')
op2 = types.KeyboardButton(text='/Tópicos')
op3 = types.KeyboardButton(text='/Atividades para prática')
option_buttons.add(
    op1,
    op2,
    op3
)

topicos_buttons = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
bt1 = types.KeyboardButton(text='/Introducao')
bt2 = types.KeyboardButton(text='/Conceitos')
bt3 = types.KeyboardButton(text='/Estrutura')
bt4 = types.KeyboardButton(text='/Funções')
bt5 = types.KeyboardButton(text='/Orientação')
bt6 = types.KeyboardButton(text='/Manipulação')
bt7 = types.KeyboardButton(text='/Tratamento')
bt8 = types.KeyboardButton(text='/Módulos')
bt9 = types.KeyboardButton(text='/Manipulaçao')
bt10 = types.KeyboardButton(text='/Testes')
bt11 = types.KeyboardButton(text='/Ambientes')
bt12 = types.KeyboardButton(text='/Frameworks')
topicos_buttons.add(
    bt1,
    bt2,
    bt3,
    bt4,
    bt5,
    bt6,
    bt7,
    bt8,
    bt9,
    bt10,
    bt11,
    bt12
)

ct1_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
ct1 = types.KeyboardButton(text='/Conceitos básicos')
ct1_buttons.add(
    ct1
)

ct2_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
ct2 = types.KeyboardButton(text='/Estrutura de dados')
ct2_buttons.add(
    ct2
)

ct3_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
ct3 = types.KeyboardButton(text='/Funções')
ct3_buttons.add(
    ct3
)

ct4_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
ct4 = types.KeyboardButton(text='/Orientação a objetos')
ct4_buttons.add(
    ct4
)

ct5_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
ct5 = types.KeyboardButton(text='/Manipulação de arquivos')
ct5_buttons.add(
    ct5
)

ct6_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
ct6 = types.KeyboardButton(text='/Tratamento de exceções')
ct6_buttons.add(
    ct6
)

ct7_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
ct7 = types.KeyboardButton(text='/Módulos e Pacotes')
ct7_buttons.add(
    ct7
)

ct8_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
ct8 = types.KeyboardButton(text='/Manipulaçao de Strings')
ct8_buttons.add(
    ct8
)

ct9_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
ct9 = types.KeyboardButton(text='/Testes e depuração')
ct9_buttons.add(
    ct9
)

ct10_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
ct10 = types.KeyboardButton(text='/Ambientes Virtuais')
ct10_buttons.add(
    ct10
)

ct11_buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
ct11 = types.KeyboardButton(text='/Frameworks e Bibliotecas Populares')
ct11_buttons.add(
    ct11
)

fl_pt1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
fl1 = types.KeyboardButton(text='/Finalizar')
fl_pt1.add(
    fl1
)

fl_pt2 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
fl2 = types.KeyboardButton(text='/Atividades')
fl_pt2.add(
    fl2
)