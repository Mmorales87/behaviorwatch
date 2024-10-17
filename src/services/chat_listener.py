import json
import time
from interfaces.ichat_listener import IChatListener
from models.insult_list import InsultList

class ChatListener(IChatListener):
    def __init__(self, config_file):
        self.insult_list = InsultList(config_file).get_insults()
        self.is_monitoring = False

    def monitor_chat(self):
        self.is_monitoring = True
        print("Monitoreando el chat...")
        while self.is_monitoring:
            # Simulación de la lectura del chat
            chat_message = self.get_chat_message()  # Método simulado para obtener mensajes del chat
            if self.check_insult(chat_message):
                user = self.get_user_from_message(chat_message)  # Método simulado para obtener el usuario
                print(f"Insulto detectado: {chat_message} de {user}")
                # Aquí puedes agregar la lógica para manejar el insulto detectado

            time.sleep(1)  # Espera un segundo antes de verificar nuevamente

    def stop(self):
        self.is_monitoring = False
        print("Deteniendo el monitoreo del chat.")

    def check_insult(self, message):
        return any(insult in message for insult in self.insult_list)

    def get_chat_message(self):
        # Simulación de un mensaje de chat
        return "Este es un mensaje de prueba con un insulto: gilipollas"

    def get_user_from_message(self, message):
        # Simulación de obtener el usuario del mensaje
        return "UsuarioPrueba"

