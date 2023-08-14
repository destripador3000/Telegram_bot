from config import * #Este es un archivo privado en donde tengo guardado el token de telegram y los chats id's
import telebot
import threading


bot =telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["inicio","ayuda","libros", "cursos","trucos"])
def cmd_start(message):
     if message.text.startswith("/libros"):
          
          bot.send_message(CHAT_ID,"A Continuación se enviarán tres libros pro favor paciencia...")
          bot.send_chat_action(message.chat.id, "upload_document")
          libro=open(".\libros\Puertos_comunes.pdf","rb")
          bot.send_document(message.chat.id, libro, caption="Puertos Comunes en ciberseguridad")
          libro2=open(".\libros\Python_Cheatsheet.pdf","rb")
          bot.send_document(message.chat.id, libro2, caption="Python")
          libro3=open(".\libros\Reverse_Shell.pdf","rb")
          bot.send_document(message.chat.id, libro3, caption="Reverse Shell")

     elif message.text.startswith("/cursos"):
        bot.send_chat_action(message.chat.id, "typing") 
        bot.reply_to(message,"https://www.freecodecamp.org/learn/information-security/")
     elif message.text.startswith("/trucos"):
          bot.send_chat_action(message.chat.id, "upload_document")
          archivo = open(".\libros\Bash_Cheatsheet.pdf","rb")
          bot.send_document(message.chat.id, archivo, caption="Trucos en Bash")
     else: 
        bot.reply_to(message, "Asegurate de interactuar a través de la línea de comandos")
        
       
       
                 
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text.startswith("/"): 
        bot.send_message(message.chat.id, "Este comando no está disponible")
    else:
        bot.send_message(message.chat.id, "Navega con cuidado")    




def mensajes():
    bot.infinity_polling()


     
if __name__ == '__main__':
    bot.set_my_commands([
        
        telebot.types.BotCommand("/inicio", "Da las instrucciones de como moverse con el bot"),
        
        telebot.types.BotCommand("/ayuda", "Da las instrucciones de como moverse con el bot"),
        telebot.types.BotCommand("/libros", "Muestra a el usuario los libros disponibles"),
        telebot.types.BotCommand("/cursos", "Le recomienda al usuario cursos gratuitos"),
        telebot.types.BotCommand("/trucos", "Muestra al usuario una lista de trucos de algunos Sistemas Operativos"),
        
    ])
    print("Iniciando bot")
    hilo_bot=threading.Thread(name="hilo_bot", target=mensajes)
    hilo_bot.start()

    print('Bot Iniciado')
    bot.send_message(CHAT_ID, "Hola cibernauta")