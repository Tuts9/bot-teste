import telebot
from telebot import types
from time import sleep
import btns

CHAVE_API = '6325756199:AAHCDh0knm4VujclwAxxQQpAwiQwqtzgjZ8'

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['Tópicos'])
def top(mensagem: types.Message):
    texto1 = """
Qual tópico você quer?
(Clique em uma opção)"""
    bot.send_message(mensagem.from_user.id, texto1, reply_markup=btns.topicos_buttons)

@bot.message_handler(commands=['Introducao', 'Começar'])
def intro(mensagem: types.Message):
    titulo = "Introdução ao Python"
    bot.send_message(mensagem.chat.id, titulo)
    sleep(2.5)
    texto1 = """
    O Python é uma linguagem de programação de alto nível, conhecida por sua sintaxe simples e legibilidade."""
    bot.send_message(mensagem.chat.id, texto1)
    sleep(5)
    texto2 = """
    Filosofia do Python, destacando os princípios como 'legibilidade conta' e 'explícito é melhor que implícito'."""
    bot.send_message(mensagem.chat.id, texto2)
    sleep(5)
    texto3 = """
    Instalação do Python e configuração do ambiente de desenvolvimento. (https://python.org.br/instalacao-windows/)"""
    bot.send_message(mensagem.chat.id, texto3, reply_markup=btns.ct1_buttons)

@bot.message_handler(commands=['Conceitos'])
def concept(mensagem: types.Message):
    titulo = "Conceitos básicos"
    bot.send_message(mensagem.chat.id, titulo)
    sleep(2.5)
    texto1 = """
- VÁRIAVEIS E TIPOS DE DADOS:
Variáveis armazenam informações; tipos incluem inteiros, floats, strings e booleanos."""
    bot.send_message(mensagem.chat.id, texto1)
    sleep(5)
    texto2 = """
- OPERADORES:
Utilização de operadores aritméticos para cálculos e operadores de comparação para avaliações condicionais."""
    bot.send_message(mensagem.chat.id, texto2)
    sleep(5)
    texto3 = """
- ESTRUTURAS DE CONTROLE DE FLUXO:
Uso de condicionais (if, elif, else) para tomadas de decisão.

Utilização de loops (for, while) para iterações."""
    bot.send_message(mensagem.chat.id, texto3, reply_markup=btns.ct2_buttons)

@bot.message_handler(commands=['Estrutura'])
def estructure(mensagem: types.Message):
    titulo = "Estrutura de Dados"
    bot.send_message(mensagem.chat.id, titulo)
    sleep(2.5)
    texto1 = """
- LISTAS, TUPLAS E DICIONÁRIOS:
Listas são sequências mutáveis, tuplas são sequências imutáveis, e dicionários armazenam pares chave-valor.

Manipulação de elementos em listas, acesso a itens em tuplas e operações com dicionários."""
    bot.send_message(mensagem.chat.id, texto1, reply_markup=btns.ct3_buttons)

@bot.message_handler(commands=['Funções'])
def func(mensagem: types.Message):
    titulo = "Funções"
    bot.send_message(mensagem.chat.id, titulo)
    sleep(2.5)
    texto1 = """
- DEFINIÇÃO E CHAMADA DE FUNÇÕES:
Funções são blocos de código reutilizáveis; definição com def e chamada com parênteses."""
    bot.send_message(mensagem.chat.id, texto1)
    sleep(5)
    texto2 = """
- PARÂMETROS E ARGUMENTOS:
Parâmetros são variáveis na definição da função; argumentos são os valores passados durante a chamada."""
    bot.send_message(mensagem.chat.id, texto2)
    sleep(5)
    texto3 = """
- RETORNO DE VALORES:
Funções podem retornar valores usando a instrução 'return'."""
    bot.send_message(mensagem.chat.id, texto3, reply_markup=btns.ct4_buttons)

@bot.message_handler(commands=['Orientação'])
def orient(mensagem: types.Message):
    titulo = "Orientação a objetos"
    bot.send_message(mensagem.chat.id, titulo)
    sleep(2.5)
    texto1 = """
- CONCEITOS BÁSICOS:
Classes são estruturas para criar objetos; objetos têm atributos e métodos.

Encapsulamento, que protege os detalhes internos de uma classe."""
    bot.send_message(mensagem.chat.id, texto1)
    sleep(5)
    texto2 = """
- HERANÇA E POLIMORFISMO:
Herança permite que uma classe herde atributos e métodos de outra.

Polimorfismo permite que objetos de diferentes classes sejam tratados de maneira uniforme."""
    bot.send_message(mensagem.chat.id, texto2, reply_markup=btns.ct5_buttons)

@bot.message_handler(commands=['Manipulação'])
def mani(mensagem: types.Message):
    titulo = "Manipulação de Arquivos"
    bot.send_message(mensagem.chat.id, titulo)
    sleep(2.5)
    texto1 = """
- LEITURA E ESCRITA DE ARQUIVOS:
Métodos para abrir, ler e escrever em arquivos.

Utilização de blocos 'with' para garantir o fechamento adequado do arquivo."""
    bot.send_message(mensagem.chat.id, texto1)
    sleep(5)
    texto2 = """
- TIPOS DE ARQUIVOS:
Trabalho com diferentes tipos, como texto, CSV e JSON."""
    bot.send_message(mensagem.chat.id, texto2, reply_markup=btns.ct6_buttons)

@bot.message_handler(commands=['Tratamento'])
def trat(mensagem: types.Message):
    titulo = "Tratamento de Exceções"
    bot.send_message(mensagem.chat.id, titulo)
    sleep(2.5)
    texto1 = """
- IDENTIFICAÇÃO E TRATAMENTO DE ERROS:
Identificação de exceções e uso de blocos 'try' e 'except'.

Exceções personalizadas para casos específicos."""
    bot.send_message(mensagem.chat.id, texto1)
    sleep(5)
    texto2 = """
- BOAS PRÁTICAS:
Utilização precisa do tratamento de exceções; evitar capturar exceções genéricas."""
    bot.send_message(mensagem.chat.id, texto2, reply_markup=btns.ct7_buttons)

@bot.message_handler(commands=['Módulos'])
def mod(mensagem: types.Message):
    titulo = "Módulos e Pacotes"
    bot.send_message(mensagem.chat.id, titulo)
    sleep(2.5)
    texto1 = """
- IMPORTAÇÃO E USO DE MÓDULOS:
Como importar bibliotecas e módulos externos.

Uso de funções e classes de módulos importados."""
    bot.send_message(mensagem.chat.id, texto1)
    sleep(5)
    texto2 = """
- ORGANIZAÇÃO DE CÓDIGOS EM PACOTES:
Agrupamento lógico de módulos em pacotes.

Estrutura de diretórios e arquivos para organizar projetos."""
    bot.send_message(mensagem.chat.id, texto2, reply_markup=btns.ct8_buttons)

@bot.message_handler(commands=['Manipulaçao'])
def maniStr(mensagem: types.Message):
    titulo = "Manipulação de Strings"
    bot.send_message(mensagem.chat.id, titulo)
    sleep(2.5)
    texto1 = """
- MÉTODOS DE MANIPULAÇÃO DE STRINGS:
Uso de métodos como 'split', 'join', 'replace' para manipulação eficaz.

Formatação de strings usando f-strings e 'format'"""
    bot.send_message(mensagem.chat.id, texto1)
    sleep(5)
    texto2 = """
- EXPRESSÕES REGULARES:
Padrões de busca em strings usando expressões regulares.

Aplicações práticas na validação e extração de padrões."""
    bot.send_message(mensagem.chat.id, texto2, reply_markup=btns.ct9_buttons)

@bot.message_handler(commands=['Testes'])
def test(mensagem: types.Message):
    titulo = "Testes e Depuração"
    bot.send_message(mensagem.chat.id, titulo)
    sleep(2.5)
    texto1 = """
- DESENVOLVIMENTO ORIENTADO A TESTES (TDD):
Criação de testes antes da implementação para garantir a funcionalidade.

Uso de frameworks de teste como 'unittest' ou 'pytest'."""
    bot.send_message(mensagem.chat.id, texto1)
    sleep(5)
    texto2 = """
- FERRAMENTAS DE DEPURAÇÃO:
Utilização de ferramentas como 'pdb' para identificar e corrigir erros."""
    bot.send_message(mensagem.chat.id, texto2, reply_markup=btns.ct10_buttons)

@bot.message_handler(commands=['Ambientes'])
def amb(mensagem: types.Message):
    titulo = "Ambientes Virtuais"
    bot.send_message(mensagem.chat.id, titulo)
    sleep(2.5)
    texto1 = """
- CRIAÇÃO E GERENCIAMENTO:
Utilização do 'venv' para criar ambientes virtuais.

Ativação e desativação de ambientes virtuais."""
    bot.send_message(mensagem.chat.id, texto1)
    sleep(5)
    texto2 = """
- DEPENDÊNCIAS E CONTROLE DE VERSÕES:
Utilização de arquivos 'requirements.txt' para listar dependências.

Integração com sistemas de controle de versão, como Git."""
    bot.send_message(mensagem.chat.id, texto2, reply_markup=btns.ct11_buttons)

@bot.message_handler(commands=['Frameworks'])
def frw(mensagem: types.Message):
    titulo = "Frameworks e Bibliotecas Populares"
    bot.send_message(mensagem.chat.id, titulo)
    sleep(2.5)
    texto1 = """
- NumPy e Pandas:
Manipulação eficiente de arrays e dataframes para processamento de dados."""
    bot.send_message(mensagem.chat.id, texto1)
    sleep(5)
    texto2 = """
- Flask:
Desenvolvimento de aplicativos web simples e eficazes.

Roteamento, templates e interação com bancos de dados."""
    bot.send_message(mensagem.chat.id, texto2, reply_markup=btns.fl_pt1)

@bot.message_handler(commands=['Finalizar'])
def final(mensagem: types.Message):
    texto1 = """
Parabéns por ter finalizado toda parte teórica.
Que tal praticar um pouco agora fazendo algumas atividades envolvendo todo conteúdo visto anteriormente?
Só clicar no botão abaixo"""
    bot.send_message(mensagem.chat.id, texto1, reply_markup=btns.fl_pt2)

@bot.message_handler(commands=['Atividades'])
def activity(mensagem: types.Message):
    texto = "Ainda em produção, volte mais tarde"
    bot.send_message(mensagem.chat.id, texto)


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem: types.Message):
    texto = """
Olá, seja bem vindo ao Bot do Tuts

--Aqui você irá aprender Python--

Escolha uma opção para continuar 

(Clique no botão abaixo)

**Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto, reply_markup=btns.option_buttons)

bot.polling()