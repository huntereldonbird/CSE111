import pytest
import Game_Grapher
import pandas as pd


def test_GetWinRate():
    assert Game_Grapher.GetWinRate(10, 5) == 50, \
        "FAILED"
    

def test_GetPlayerInfo():

    file = pd.read_csv("Score.csv")\

    wins, games = Game_Grapher.GetPlayerInfo(file, "Maddy")

    assert games == 5, \
        "FAILED"




pytest.main(["-v", "--tb=line", "-rN", __file__])
