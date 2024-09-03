from pythontextnow import Client
from pythontextnow import ConversationService
from datetime import datetime, timezone

USERNAME = "yerong_li"
SID_COOKIE = "s%3AWtvbjiF62-17-hQrCuCGmD7fYydyQLKi.g6ukTTxg4FPNcKbG9hsnWY2CN2OiOHgF1O0LSGmhftY"

Client.set_client_config(username=USERNAME, sid_cookie=SID_COOKIE)

PHONE_NUMBER_1 = "+16266398503"
conversation_service = ConversationService(conversation_phone_numbers=[PHONE_NUMBER_1])


current_datetime = datetime.now(timezone.utc)
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S %Z")
message = f"Hello World! Current date and time (UTC): {formatted_datetime}"
print(message)
# message = 'Hello'
# conversation_service.send_message(message=message)
messages_generator = conversation_service.get_messages(num_messages=30)

last_10_messages = list()
for message_list in messages_generator:
    last_10_messages += message_list