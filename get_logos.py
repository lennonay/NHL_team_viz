import matplotlib.gridspec as gridspec
import pandas as pd
import os
import matplotlib.pyplot as plt
from PIL import Image
import requests

def main():
    url = 'https://raw.githubusercontent.com/lennonay/NHL_team_viz/main/data/team_names.csv'
    team_name = pd.read_csv(url)

    gs1 = gridspec.GridSpec(6, 6)

    if not os.path.exists("logos"):
        os.makedirs("logos")

    for i in range(len(team_name)):
        ax1 = plt.subplot(gs1[i])
        abr = (team_name.iloc[i]['Abrv_espn'])
        path = 'https://a.espncdn.com/i/teamlogos/nhl/500/' + abr +'.png'
        im = Image.open(requests.get(path, stream=True).raw)
        image_name = 'logos/' + abr + '.png'
        im.save(image_name)
        ax1.imshow(im)
        plt.gca().axis('off')
    
    plt.savefig('data/teams.png')

if __name__ == "__main__":
    main()