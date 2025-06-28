from unittest.mock import patch
import time

class timeMock:
    @staticmethod
    def choix_heure(hour):
        # Crée un mock pour retourner une heure spécifique
        mock_localtime = patch('time.localtime').start()
        mock_localtime.return_value = time.struct_time((2000, 1, 1, hour, 0, 0, 0, 0, 0))
        return mock_localtime

    @staticmethod
    def stop_mock(mock):
        patch.stopall()