import argparse
import json
from z3c.rml import rml2pdf
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Local imports
from utils import *

DEFAULT_FILENAME = 'sample'
DEFAULT_TEMPLATE = 'cv-one-column-default.xml'
DEFAULT_DATA = 'data/sample/data.json'
TEMPLATES_DIR = 'templates'
OUTPUT_DIR = 'output'

env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=select_autoescape()
)

def get_template(template_name):
    template = env.get_template(template_name)
    template.globals['now'] = now
    template.globals['datetime_convert'] = datetime_convert

    return template

def openJsonData(input_data):

    with open(f'{input_data}', 'r') as f:
        data = json.load(f)

    content = data['content']
    settings = data['settings']
    return content, settings


def main(input_data, template_name, out_name):

    path_to_save = f'{OUTPUT_DIR}/{out_name}.pdf'

    content, settings = openJsonData(input_data)

    template = get_template(template_name)

    input_dir = '/'.join(input_data.split('/')[:-1])
    xml_data = template.render(input_dir=input_dir, out_name=out_name, content=content, settings=settings)

    io_data = rml2pdf.parseString(xml_data, removeEncodingLine=True, filename=out_name)

    with open(path_to_save,'wb') as f:
        f.write(io_data.getbuffer())

    print(f'{out_name}.pdf was successful created in {path_to_save}')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='cv-generator')

    parser.add_argument('input_data', nargs='?', default=DEFAULT_DATA,
        help='Path where data.json is stored')
    parser.add_argument('-o', '--output', dest='file', nargs='?', default=DEFAULT_FILENAME,
        help='PDF Filename that will be stored inside ./output/')
    parser.add_argument('-t', '--template', dest='template_name', nargs='?', 
        default=DEFAULT_TEMPLATE,
        help='xml file name to use like template. It should be stored inside ./templates/')

    args = parser.parse_args()
    main(
        args.input_data, 
        args.template_name,
        args.file
    )