import pandas as pd

def GetWinRate(games, wins):
    pass



def GetPlayerInfo(df, playerName):
    Wins = 0
    Games = 0

    for x in range(0, df.shape[1]):
        cell = df.iloc[4, x]

        if((cell == "Rebel Win") or (cell == "Empire Win") or (cell == "Const Win")):
            print("WINNER")
            Wins += 1
            Games += 1
        if((cell == "Rebel Loss") or (cell == "Empire Loss") or (cell == "Const Loss")):
            print("LOSER")
            Games += 1

    return Wins, Games


def main():
    df = pd.read_csv("Score.csv")

    wins, loss = GetPlayerInfo(df, "Eldon")

    print(f"Wins: {wins}, Loss: {loss}")




if __name__ == "__main__":
    main()