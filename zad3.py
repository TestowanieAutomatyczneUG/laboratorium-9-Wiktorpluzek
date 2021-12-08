import unittest
from unittest.mock import *
from datetime import datetime

class Alarm:
    def getTime(self):
        return datetime.now()

    def playWavFile(self, file):
        pass

class Checker:
    def __init__(self, clock):
        self.alarm = clock
        self.was_played = False

    def was_played(self):
        return self.was_played

    def wavWasPlayed(self):
        self.was_played = True

    def resetWav(self):
        self.was_played = False

    def remainder(self):
        if self.alarm.getTime().hour >= 17:
            self.alarm.playWavFile("Ring.wav")
            self.wavWasPlayed()

class TestChecker(unittest.TestCase):

    def testPlayed(self):
        clock = Alarm()
        clock.getTime = Mock(name="getTime")
        clock.getTime.return_value = datetime(2021, 6, 12, 19, 0, 0, 0)
        clockChecker = Checker(clock)
        clockChecker.remainder()
        self.assertTrue(clockChecker.was_played)

    def testNotPlayed(self):
        clock = Alarm()
        clock.getTime = Mock(name="getTime")
        clock.getTime.return_value = datetime(2021, 6, 12, 15, 0, 0, 0)
        clockChecker = Checker(clock)
        clockChecker.remainder()
        self.assertFalse(clockChecker.was_played)
