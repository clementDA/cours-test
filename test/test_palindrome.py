import unittest
from src.ohce import OHCE
from utilities.testBuilder import OHCEBuilder
from src.language import LANGUAGES
from utilities.timemock import timeMock



#classe de tests de la fonction palindrome
class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.builder = OHCEBuilder()

    
    def test_palindrome_palindrome(self):
        #ETANT DONNE un utilisateur par defaut
        ohce = self.builder.build()

        #QUAND on saisit un palindrome
        resultat=ohce.palindrome("radar")

        #ALORS on affiche les felicitation par defaut
        attendu = LANGUAGES[""]["felicitation"]
        self.assertIn(attendu, resultat)


    def test_palindrome_vide(self):
        #ETANT DONNE un utilisateur par defaut
        ohce = self.builder.build()

        #QUAND on saisi une entre vide
        resultat=ohce.palindrome("")
        
        #ALORS on affiche les felicitation par defaut
        self.assertIn("felicitation", resultat)

    def test_palindrome_sans_entre(self):
        #ETANT DONNE un utilisateur par defaut
        ohce = self.builder.build()

        #QUAND on saisi une entre vide
        #ALORS on soulève une erreur
        with self.assertRaises(TypeError):
             ohce.palindrome(None)
        
       
    def test_palindrome_entre_mauvais_type(self):
        #ETANT DONNE un utilisateur par defaut
        ohce = self.builder.build()

        #QUAND on saisi une entre de type non string
        #ALORS on soulève une erreur
        with self.assertRaises(TypeError):
             ohce.palindrome(42)
        
       

    def test_palindrome_speciaux(self):
        #ETANT DONNE un utilisateur par defaut
        ohce = self.builder.build()

        #QUAND on saisit un palindrome comprenant un caractere special
        resultat=ohce.palindrome("ra#ar")
        
        #ALORS on affiche les felicitation par defaut
        self.assertIn("felicitation", resultat)

    def test_non_palindrome_speciaux(self):
        #ETANT DONNE un utilisateur par defaut
        ohce = self.builder.build()

        #QUAND on saisit un non palindrome comprenant un caractere special
        resultat=ohce.palindrome("#ar")
        
        #ALORS on affiche le miroir du message saisi avec le caractere special
        self.assertIn("ra#", resultat)

    def test_palindrome_casse(self):
        #ETANT DONNE un utilisateur par defaut
        ohce = self.builder.build()

        #QUAND on saisit un palindrome mais comprenant une majuscule
        resultat=ohce.palindrome("Radar")
        
        #ALORS on affiche le miroir du message saisi le palindrome car sensible à la casse
        self.assertIn("radaR", resultat)

    def test_non_palindrome_casse(self):
        #ETANT DONNE un utilisateur par defaut
        ohce = self.builder.build()

        #QUAND on saisit un non palindrome comprenant une majuscule
        resultat=ohce.palindrome("nipaL")
        
        #ALORS on affiche le miroir du message saisi avec le caractere special
        self.assertIn("Lapin", resultat)

  

    def test_non_palindrome(self):
        #ETANT DONNE un utilisateur par defaut
        ohce = self.builder.build()

        #QUAND on ne saisit pas un palindrome
        resultat= ohce.palindrome("lapin")

        #ALORS on affiche le miroir du message saisi
        self.assertIn("nipal",resultat)


    def test_non_palindrome_nombre(self):
        #ETANT DONNE un utilisateur par defaut
        ohce = self.builder.build()

        #QUAND on saisit un non palindrome comprenant des chiffres
        resultat= ohce.palindrome("3lapin")

        #ALORS on affiche le miroir du message saisi
        self.assertIn("nipal3",resultat)


    def test_palindrome_nombre(self):
        #ETANT DONNE un utilisateur par defaut
        ohce = self.builder.build()

        #QUAND on saisit un palindrome comprenant des chiffres
        resultat= ohce.palindrome("32kayak23")

        #ALORS on affiche le message de felicitation
        attendu = LANGUAGES[""]["felicitation"]
        self.assertIn(attendu, resultat)



    def test_initialisation_langue(self):
        #ETANT DONNE un utilisateur parlant une langue enregistré
        langue = "fr"
        ohce = self.builder.with_language(langue).build()

        #QUAND on saisis n'improtequoi
        resultat = ohce.palindrome("test")
        #ALORS on recois un résultat
        self.assertIsInstance(resultat, str)
        


    def test_aurevoir_langue_connu(self):
        #ETANT DONNE un utilisateur parlant une langue connue
        langue = "fr"
        ohce = self.builder.with_language(langue).build()

        #QUAND on saisis n'improtequoi
        resultat =  ohce.palindrome("test")

        #ALORS on affiche les adieu de la langue associé
        attendu = LANGUAGES[langue]["adieu"]
        self.assertIn(attendu, resultat)

    def test_felicitation_langue_connu(self):
        #ETANT DONNE un utilisateur parlant une langue connue
        langue = "fr"
        ohce = self.builder.with_language(langue).build()

        #QUAND on saisit un palindrome
        resultat=ohce.palindrome("radar")

        #ALORS on affiche les felicitation de la langue associé
        attendu = LANGUAGES[langue]["felicitation"]
        self.assertIn(attendu, resultat)

    def test_langage_inconnu(self):
        #ETANT DONNE un utilisateur parlant une langue inconnue
        langue="uknow"
        #QUAND on crée l'objet
        #ALORS on recois un message d'erreur
        with self.assertRaises(ValueError):
            ohce = self.builder.with_language(langue).build()

    def test_format_message(self):
        #ETANT DONNE un utilisateur parlant une langue connue
         langue = "fr"
         ohce = self.builder.with_language(langue).build()
         mock = timeMock.choix_heure(10)


        #QUAND on appelle la fonction
         resultat=ohce.palindrome("test")


         timeMock.stop_mock(mock)
        #ALORS Le message commence par la salutation
         self.assertTrue(resultat.startswith(LANGUAGES[langue]["salutation_am"]))
        # Et finit par l’adieu
         self.assertTrue(resultat.strip().endswith(LANGUAGES[langue]["adieu"]))


    def test_bonjour_matin(self):
        # ETANT DONNE un utilisateur parlant une langue connue
        langue = "en"
        ohce = self.builder.with_language(langue).build()

        # ET nous somme le matin
        mock = timeMock.choix_heure(10)

        # QUAND on saisit n'importe quoi
        resultat = ohce.palindrome("test")

        # ALORS on affiche les salutations de la langue associée au matin
        attendu = LANGUAGES[langue]["salutation_am"]
        timeMock.stop_mock(mock)
        self.assertIn(attendu, resultat)


    def test_bonjour_apres_midi(self):
        # ETANT DONNE un utilisateur parlant une langue connue
        langue = "en"
        ohce = self.builder.with_language(langue).build()

        # ET nous somme l'après-midi
        mock = timeMock.choix_heure(15)
        
        # QUAND on saisit n'importe quoi
        resultat = ohce.palindrome("test")

        # ALORS on affiche les salutations de la langue associée a l'apres midi
        attendu = LANGUAGES[langue]["salutation_pm"]
        timeMock.stop_mock(mock)
        self.assertIn(attendu, resultat)


    def test_bonjour_nuit(self):
        # ETANT DONNE un utilisateur parlant une langue connue
        langue = "en"
        ohce = self.builder.with_language(langue).build()

        # ET nous somme le soir
        mock = timeMock.choix_heure(23)

        # QUAND on saisit n'importe quoi
        resultat = ohce.palindrome("test")

        # ALORS on affiche les salutations de la langue associée au soir
        attendu = LANGUAGES[langue]["salutation_nuit"]
        timeMock.stop_mock(mock)
        self.assertIn(attendu, resultat)



    def test_bonjour_matin_limite(self):
        # ETANT DONNE un utilisateur parlant une langue connue
        langue = "en"
        ohce = self.builder.with_language(langue).build()

        # ET nous somme a la premiere minute du matin
        mock = timeMock.choix_heure(4)

        # QUAND on saisit n'importe quoi
        resultat = ohce.palindrome("test")

        # ALORS on affiche les salutations de la langue associée au matin
        attendu = LANGUAGES[langue]["salutation_am"]
        timeMock.stop_mock(mock)
        self.assertIn(attendu, resultat)


    def test_bonjour_apres_midi_limite(self):
        # ETANT DONNE un utilisateur parlant une langue connue
        langue = "en"
        ohce = self.builder.with_language(langue).build()

        # ET nous somme a la première minute de l'après midi
        mock = timeMock.choix_heure(12)
        
        # QUAND on saisit n'importe quoi
        resultat = ohce.palindrome("test")

        # ALORS on affiche les salutations de la langue associée a l'apres midi
        attendu = LANGUAGES[langue]["salutation_pm"]
        timeMock.stop_mock(mock)
        self.assertIn(attendu, resultat)


    def test_bonjour_nuit_limite(self):
        # ETANT DONNE un utilisateur parlant une langue connue
        langue = "en"
        ohce = self.builder.with_language(langue).build()

        # ET nous somme a la première minute de la nuit
        mock = timeMock.choix_heure(20)

        # QUAND on saisit n'importe quoi
        resultat = ohce.palindrome("test")

        # ALORS on affiche les salutations de la langue associée au soir
        attendu = LANGUAGES[langue]["salutation_nuit"]
        timeMock.stop_mock(mock)
        self.assertIn(attendu, resultat)



    def test_etat_sans_changement(self):
         # ETANT DONNE un utilisateur parlant une langue française
          langue = "fr"
          ohce = self.builder.with_language(langue).build()

          # ET on capture son état interne
          ancienne_langue = ohce.language
          anciens_messages = ohce.messages.copy()

          # QUAND on appelle la méthode palindrome
          ohce.palindrome("radar")

          # ALORS la langue et les messages ne changent pas
          self.assertEqual(ohce.language, ancienne_langue)
          self.assertEqual(ohce.messages, anciens_messages)

if __name__ == '__main__':
    unittest.main()
