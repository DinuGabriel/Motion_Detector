# Import necessary libraries
from motion_detector import df  # Assuming you have a "motion_detector" module with your DataFrame
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

# Convert the "Start" and "End" columns to string format for display
df["Start_string"] = df["Start"].dt.strftime('%Y-%m-%d %H:%M:%S')
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

# Create a ColumnDataSource to work with Bokeh
cds = ColumnDataSource(df)

# Create a Bokeh figure for the motion graph
p = figure(x_axis_type="datetime", height=100, width=500, responsive=True, title="Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

# Add a HoverTool for tooltips showing the start and end times
hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

# Create a bar (quad) glyph to represent motion events
q = p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)

# Specify the output file name for the HTML visualization
output_file("Graph.html")

# Show the Bokeh plot
show(p)
