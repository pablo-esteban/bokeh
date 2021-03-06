from bokeh.models.tools import BoxZoomTool, ResetTool
from bokeh.plotting import figure, output_file, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# set output to static HTML file
output_file("first_steps.html")

# create a plot
p = figure(
    title="Specifying tools example",
    tools=[BoxZoomTool(), ResetTool()],
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
)

# add a renderer
p.circle(x, y, size=10)

# show the results
show(p)
