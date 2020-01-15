import vk_api
import time

delay = 600
chat = '' # 2000000000+id чата из ссылки
token = '' # От Кейта
text = '' # Что шлём
vk_session = vk_api.VkApi(token = token)
vk = vk_session.get_api()

while True:
    vk.messages.send(peer_id = chat, message = text, random_id = time.time())
    time.sleep(delay)
