import pandas as pd

def GetWinRate(games, wins):
    
    val = round((wins / games) * 100)

    return val

def LoadDataFrame(fileName):

    df = pd.read_csv(fileName)
    return df



def GetPlayerInfo(df, playerName):
    Wins = 0
    Games = 0

    row_index = df.index[df['Players'] == playerName].tolist()

    for x in range(0, df.shape[1]):
        cell = df.iloc[row_index[0], x]

        if((cell == "Rebel Win") or (cell == "Empire Win") or (cell == "Const Win")):
            print("WINNER")
            Wins += 1
            Games += 1
        if((cell == "Rebel Loss") or (cell == "Empire Loss") or (cell == "Const Loss")):
            print("LOSER")
            Games += 1

    return Wins, Games


def main():

    playerIn = input("Which player Do you want info for : ")
    
    df = LoadDataFrame("Score.csv")

    wins, games = GetPlayerInfo(df, playerIn)

    percent = GetWinRate(games, wins)

    print(f"Wins: {wins}, Games: {games} with a win% of, {percent}%")



if __name__ == "__main__":
    main()