# Strings
from datetime import datetime


class Notification:
    def __init__(
        self, 
        from_addr: str,
        to_addr: str,
        subject: str,
        message: str) -> None:
        
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self._message = message

    def message(self):
        return self._message



# Driver code 
# email = Notification(
#     'teddy@gmail.com',
#     'info@kofiteddy.com',
#     'Comments on the Chapter',
#     'Can we emphasize Python 3.9 type hints'
# )
# formatted = f''' 
#             from: <{email.from_addr}>
#             to: <{email.to_addr}>
#             subject: {email.subject}
#             {email.message()}
#             '''

important = datetime(2022, 2, 7, 13, 14)
print(f'{important:%Y-%m-%d %I:%M%p}')



