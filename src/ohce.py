class OHCE:
    def __init__(self, language):
        self.language= language
        pass

    def __greeting(self) -> str:
        return "Bonjour \n"

    def palindrome(self, text: str) -> str:
        retour = self.__greeting()

        if text == text[::-1]:
            retour += "Bien dit! \n"
        else:
            retour += text[::-1]
        return retour + "\nAu revoir"
