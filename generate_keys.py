#!/usr/bin/python

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

def slice_it(li, cols=2):
    start = 0
    for i in range(cols):
        stop = start + len(li[i::cols])
        yield li[start:stop]
        start = stop

with open('keys.txt', 'r') as f:
    # Template
    template = env.get_template('index.html')

    structure = []
    for line in f:
        if 'Keys' in line: # New section
            tmp = {}
            current = line.strip()
            tmp['section'] = current
            tmp['keys'] = []
            structure.append(tmp)
        if ':' in line: # key binding
            line = line.strip()
            try:
                key, desc = line.split(' : ', 1)
            except ValueError:
                continue
            tmp['keys'].append('<kbd>%s</kbd> - %s' % (key.strip(), desc.strip()))

    output_from_parsed_template = template.render(data = slice_it(structure, 3))
    with open("html/index.html", 'w') as fh:
        fh.write(output_from_parsed_template)
        print("Generated cheat sheet written to html/index.html")
