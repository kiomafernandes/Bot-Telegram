import telebot
import dotenv
from os import getenv

dotenv.load_dotenv()

TOKEN_TELEGRAM = getenv('TOKEN_TELEGRAM')


bot = telebot.TeleBot(TOKEN_TELEGRAM)

comandos = (
    '/opcao1 - Tenho uma duvida',
    '/opcao2 - Gostaria de agendar um horário'
    '/opcao3 - Gostaria de desmarcar meu horário'
    '/opcao4 - Gostaria de remarcar meu horário'
)

@bot.message_handler(comandos=['start'])
def mensagem_boas_vindas(message):
    bot.send_message(message.chat.id, 'Olá, tudo bem? Escolha uma das seguintes opções:')
    bot.send_message(message.chat.id, comandos[0])
    bot.send_message(message.chat.id, comandos[1])


@bot.message_handler(comandos=['opcao1'])
def opcao1(message):
    bot.send_message(message.chat.id, 'Diga qual a sua duvida, responderei asssim que possivel!')


@bot.message_handler(comandos=['opcao2'])
def opcao2(message):
    bot.send_message(message.chat.id, 'Diga para qual serviço você gostaria de agendar um horario?')


@bot.message_handler(comandos=['opcao3'])
def opcao3(message):
    bot.send_message(message.chat.id, 'Diga para qual serviço você gostaria de agendar um horario?')


@bot.message_handler(comandos=['opcao4'])
def opcao4(message):
    bot.send_message(message.chat.id, 'Informe o horário marcado e o serviço para o qual agendou o horário!')


@bot.message_handler(func=lambda message:'Bom dia' in message.text)
def respond_usuairo(message):
    nome_usuario = message.from_user.first_name
    resposta = f'Olá, {nome_usuario}. em que posso ajudar?'
    bot.reply_to(message, resposta)


if __name__ == '__main__':
    bot.polling()


