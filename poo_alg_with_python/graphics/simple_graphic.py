from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('simple_graphic.html')
    fig = figure()

    # type(fig)

    total_vals = int(input('Number of values to be plotted: '))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = x + 2
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width = 2)
    show(fig)