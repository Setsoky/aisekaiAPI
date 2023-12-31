import requests

class aisekai:
    """
        A small API Module for https://aisekai.ai. \n
        on init provide your token found in the Authorization header \n
        (you could just make a request on the site in order to find it)
    """
    def __init__(self, token: str):
        self.URL = 'https://api.aisekai.ai/api/v1'
        self.Token = token

    def getChatId(self, charId: str):
        """
            Returns ChatID you will need it in order to send Messages \n
            with the 'createMessage' function
        """
        chatId = requests.get(f'{self.URL}/characters/{charId}/chats?size=1', headers={'Authorization': self.Token}).json()
        return chatId['_id']

    def getAllMessages(self, charId: str):
       """
            Returns All Messages written by the AI and the User \n
            You will have to provide the CharId. Its provided in the chat Url that you will find on the website.
       """
       messages = requests.get(f'{self.URL}/characters/{charId}/chats?size=99999', headers={'Authorization': self.Token}).json()
       return messages['messages']
    
    def getCharMessages(self, charId: str):
        """
            Only Returns messages written by the AI \n
            You will have to provide the CharId. Its provided in the chat Url that you will find on the website.
        """
        messages = requests.get(f'{self.URL}/characters/{charId}/chats?size=99999', headers={'Authorization': self.Token}).json()
        charMessages = []
        for i in messages['messages']:
            if i['role'] == 'assistant':
                charMessages.append(i)
        return charMessages
    
    def createMessage(self, chatId: str, message: str):
        """
            Send a Message using the function. \n
            The function will also return the AI Response. \n
            you will have to provide a message and the chatId that you can retrieve using the 'getChatId' function.
        """
        ResponseMessage = requests.post(f'{self.URL}/chats/{chatId}/messages',headers={'Authorization': self.Token}, json={
            'actions': '',
            'content': message
        })
        return ResponseMessage.json()
    
    def yourChats(self):
        """
            Returns your chats, including last messages character name, id and more
        """
        chats = requests.get(f'{self.URL}/chats', headers={'Authorization': self.Token})
        return chats.json()
    
    def trendingCharacters(self):
        """
            Returns trending characters including their information. \n
            No Authorization needed.
        """
        trending = requests.get(f'{self.URL}/characters/group')

        return trending.json()[0]['list']