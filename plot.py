import pandas as pd
import plotly.express as px
from PIL import Image

def scatter_plot(team_5v5):
    fig = px.scatter(team_5v5, x ='xGoalsFor', y = 'goalsFor', hover_name='Team', title = '5on5 goals for and expected goals for')
    fig.update_traces(marker=dict(color='rgba(0,0,0,0)'), showlegend=False)
    for i in range(len(team_5v5)):
        path = 'logos/' + team_5v5.iloc[i]['Abrv_espn'] +'.png'
        fig.add_layout_image(x = team_5v5.iloc[i]['xGoalsFor'], y = team_5v5.iloc[i]['goalsFor'], source = Image.open(path),
                xref="x",
                yref="y",
                sizex=5,
                sizey=5,
                xanchor="center",
                yanchor="middle",
            )
    fig.update_xaxes(range = [120,220])
    fig.update_yaxes(range = [120,220])
    fig.update_layout(
        autosize=False,
        width=750,
        height=750
    )
    fig.add_annotation(text="Underperforming expectation",
                    xref="paper", yref="paper",
                    x=0.95, y=0.05, showarrow=False)

    fig.add_annotation(text="Outperforming expectation",
                    xref="paper", yref="paper",
                    x=0.05, y=0.95, showarrow=False)
    fig.update_layout(shapes = [{'type': 'line','line': {'dash':'dot'}, 'yref': 'paper', 'xref': 'paper', 'y0': 0, 'y1': 1, 'x0': 0, 'x1': 1, 'layer': 'below'}])

    return fig

def main():
    team_name = pd.read_csv('data/team_names.csv',index_col=False).set_index('Abrv')
    team_data = pd.read_csv('data/team_data.csv')
    
    team_5v5 = team_data[team_data['situation']=='5on5'].set_index('team')
    team_5v5 = team_5v5.join(team_name)

    fig = scatter_plot(team_5v5)
    fig.show()

if __name__ == "__main__":
    main()