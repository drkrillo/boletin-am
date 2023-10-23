import datetime

from jinja2 import Environment, FileSystemLoader

from utils.reader import reader
from utils.preprocesser import sort_by
from utils.ranker import ranker


FILEPATH = 'data.json'

today = str(datetime.datetime.today().strftime('%Y-%m-%d'))


def main():
    data = reader(FILEPATH)
    data = ranker(data, threshold=50)
    data = sort_by(data)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('README.md.j2')
    rendered_readme = template.render(results=data, today=today, areas=set([x['area'] for x in data]))
            
    with open("README.md", "w+") as f:
        f.write(rendered_readme)

    for pub in data:
        print("********************")

if __name__ == "__main__":
    main()