import unittest
from src.ohce import OHCE
from utilities.testBuilder import OHCEBuilder
from src.language import LANGUAGES

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

        #QUAND on ne saisit rien
        resultat=ohce.palindrome("")
        
        #ALORS on affiche les felicitation par defaut
        self.assertIn("felicitation", resultat)

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
        


    def test_bonjour_langue_connu(self):
        #ETANT DONNE un utilisateur parlant une lague connue
        langue = "fr"
        ohce = self.builder.with_language(langue).build()

        #QUAND on saisis n'improtequoi
        resultat = ohce.palindrome("test")

        #ALORS on affiche les salutation de la langue associé
        attendu = LANGUAGES[langue]["salutation"]
        self.assertIn(attendu, resultat)

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

        #QUAND on appelle la fonction
         resultat=ohce.palindrome("")

        #ALORS Le message commence par la salutation
         self.assertTrue(resultat.startswith(LANGUAGES[langue]["salutation"]))
        # Et finit par l’adieu
         self.assertTrue(resultat.strip().endswith(LANGUAGES[langue]["adieu"]))



if __name__ == '__main__':
    unittest.main()
