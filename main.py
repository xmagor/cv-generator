from z3c.rml import rml2pdf
from jinja2 import Environment, FileSystemLoader, select_autoescape

DEFAULT_FILENAME = 'sample.pdf'
DEFAULT_TEMPLATE = 'one-column-default.xml'
TEMPLATES_DIR = 'templates'
OUTPUT_DIR = 'output'

env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=select_autoescape()
)
template = env.get_template(DEFAULT_TEMPLATE)

def main(filename):

    path_to_save = f'{OUTPUT_DIR}/{filename}'

    xml_data = template.render()

    io_data = rml2pdf.parseString(xml_data, removeEncodingLine=True, filename=filename)

    with open(path_to_save,'wb') as f:
        f.write(io_data.getbuffer())

    print(f'{filename} was successful created in {path_to_save}')


if __name__ == '__main__':

    filename = DEFAULT_FILENAME
    main(filename)