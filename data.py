import pandas as pd

def main():
    url = 'https://www.moneypuck.com/moneypuck/playerData/seasonSummary/2022/regular/teams.csv'
    storage_options = {'User-Agent': 'Mozilla/5.0'}
    team_data = pd.read_csv(url, storage_options = storage_options)
    team_data.to_csv('data/team_data.csv', index=False)


if __name__ == "__main__":
    main()