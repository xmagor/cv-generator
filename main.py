import argparse
import json
from z3c.rml import rml2pdf
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Local imports
from utils import *

DEFAULT_FILENAME = 'sample.pdf'
DEFAULT_TEMPLATE = 'one-column-default.xml'
DEFAULT_DATA = 'data'
TEMPLATES_DIR = 'templates'
OUTPUT_DIR = 'output'

env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=select_autoescape()
)

template = env.get_template(DEFAULT_TEMPLATE)
template.globals['now'] = now
template.globals['datetime_convert'] = datetime_convert


def openJsonData(dir_name):

    with open(f'{DEFAULT_DATA}/{dir_name}/data.json', 'r') as f:
        data = json.load(f)

    content = data['content']
    settings = data['settings']
    return content, settings


def main(dir_name, filename):

    path_to_save = f'{OUTPUT_DIR}/{filename}'

    content, settings = openJsonData(dir_name)

    xml_data = template.render(dir_name=dir_name, content=content, settings=settings)

    io_data = rml2pdf.parseString(xml_data, removeEncodingLine=True, filename=filename)

    with open(path_to_save,'wb') as f:
        f.write(io_data.getbuffer())

    print(f'{filename} was successful created in {path_to_save}')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='cv-generator')

    parser.add_argument('input_data',
        help='Directoy name inside ./data/ with data requeried by the template')
    parser.add_argument('filename_out', nargs='?', default=DEFAULT_FILENAME,
        help='PDF Filename that will be stored inside ./output/')

    args = parser.parse_args()
    main(args.input_data, args.filename_out)