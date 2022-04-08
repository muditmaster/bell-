import plotly.figure_factory as ff
import pandas as pd
import csv

yoyo = pd.read_csv("datayo.csv")

yoo = ff.create_distplot([yoyo['Avg Rating'].tolist()],['Avg Rating'] ,show_hist=False)
yoo.show()
