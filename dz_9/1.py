import time

color = {'red': 1, 'yellow': 1, 'green': 1}

last_color = None
color_list = [colors for colors in color.keys()]
for colors, delay in color.items():
    if last_color < color_list.index() or None:
        last_color = color_list.index()
        print(f'горит {colors}')
        #time.sleep(delay)
    else:
        raise ValueError('нарушен порядок следования цветов')
    break

