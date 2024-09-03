from pythontextnow import Client
from pythontextnow import ConversationService
from datetime import datetime, timezone
import time
USERNAME = "yerong_li"
SID_COOKIE = "s%3AWtvbjiF62-17-hQrCuCGmD7fYydyQLKi.g6ukTTxg4FPNcKbG9hsnWY2CN2OiOHgF1O0LSGmhftY"

Client.set_client_config(username=USERNAME, sid_cookie=SID_COOKIE)

PHONE_NUMBER_1 = "+16266398503"
# conversation_service = ConversationService(conversation_phone_numbers=[PHONE_NUMBER_1])


# current_datetime = datetime.now(timezone.utc)
# formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S %Z")
# message = f"Hello World! Current date and time (UTC): {formatted_datetime}"
# print(message)
# message = 'Hello'
# conversation_service.send_message(message=message)

# messages_generator = conversation_service.get_messages(num_messages=5)

# last_10_messages = list()
# for message_list in messages_generator:
#     last_10_messages += message_list

# ans = []
# for sms in last_10_messages:
# 	ans.append([sms.datetime_, sms.number,sms.text, sms.message_direction, sms.datetime_])
# ans[:] = sorted(ans, reverse=True)

# def remove_adjacent_duplicates(sorted_list):
#     if not sorted_list:
#         return []
    
#     result = [sorted_list[0]]
#     for element in sorted_list[1:]:
#         if element != result[-1]:
#             result.append(element)
    
#     return result
# ans = remove_adjacent_duplicates(ans)

# for sms in ans:
# 	print(sms)

def fetch_and_process_messages():
    previous_ans = None
    while True:
        conversation_service = ConversationService(conversation_phone_numbers=[PHONE_NUMBER_1])
        messages_generator = conversation_service.get_messages(num_messages=5)
        last_10_messages = list()
        for message_list in messages_generator:
            last_10_messages += message_list

        ans = []
        for sms in last_10_messages:
            ans.append([sms.datetime_, sms.number, sms.text, sms.message_direction, sms.datetime_])
        ans[:] = sorted(ans, reverse=True)

        ans = remove_adjacent_duplicates(ans)

        if previous_ans and ans:
            if previous_ans[0] != ans[0] and previous_ans[0] == ans[1]:
                print("New SMS:", ans[0])
            else:
                print(' ... ')
        elif previous_ans is None:
            print(' ... ')

        previous_ans = ans

        # time.sleep(3)

def remove_adjacent_duplicates(sorted_list):
    if not sorted_list:
        return []
    
    result = [sorted_list[0]]
    for element in sorted_list[1:]:
        if element != result[-1]:
            result.append(element)
    
    return result

fetch_and_process_messages()