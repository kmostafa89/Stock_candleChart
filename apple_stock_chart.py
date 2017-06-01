from  pandas_datareader import data
from datetime import datetime as dt
from bokeh.plotting import figure , output_file , show


start = dt(2000 , 3, 1)
end = dt.now()

df = data.DataReader(name = "AAPL", data_source = "yahoo", start = start, end = dt.now())
###AAPL is the name of the counterparty , in this case it's apple

# print(df.columns)

# print(df.shape)
# print(df.describe())

def inc_dec(c, o):
    if o < c:
        value = "inc"
    elif c < o :
        value = "dec"
    else:
        value = None
    return value

df["Status"] = [inc_dec(c, o ) for c, o in zip(df.Close, df.Open)]
df["Middle"] = (df.Open + df.Close)/2
df["diff"] = abs(df.Close - df.Open)
print(df.head())


p = figure(x_axis_type = "datetime", width =1000, height = 400 , responsive = True)
p.title = "Financial Chart"
p.grid.grid_line_alpha = 0.005

hour_12 = 12*60*60*1000
p.segment(df.index, df.High , df.index, df.Low, color = "black")# this will draw the lines of the graph
p.rect(df.index[df.Status == "inc"], df.Middle[df.Status == "inc"], hour_12 , abs(df.Close - df.Open),fill_color = "#00FF00", line_color = "black")
p.rect(df.index[df.Status =="dec"], df.Middle[df.Status =="dec"], hour_12, abs(df.Close - df.Open), fill_color = "red", line_color = "black")
output_file("test.html")
show(p)
