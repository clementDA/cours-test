from src.language import LANGUAGES

class OHCE:
    def __init__(self, language):
        self.language= language
        self.messages = self.__load_messages(language)
        pass

    def __greeting(self) -> str:
        return self.messages["salutation"]
    
    def __goodbye(self) -> str:
        return "\n"+self.messages["adieu"]
    
    def __congrat(self) ->str:
        return "\n"+self.messages["felicitation"]
    
    def __load_messages(self, language: str) -> dict:
        if language in LANGUAGES:
            return LANGUAGES[language]
        raise ValueError(f"Langue non supportée : {language}")

    def palindrome(self, text: str) -> str:
        retour = self.__greeting()

        if text == text[::-1]:
            retour += self.__congrat()
        else:
            retour += text[::-1]
        return retour + self.__goodbye()
