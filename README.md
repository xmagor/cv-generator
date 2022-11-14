# CV Generator

CV generator combining a json data file and a xml template with the Jinja2 template engine and z3c (an alternative to ReportLab's RML PDF generation XML format) to generate a customizables Curriculum vitae pdfs.


## Install

To handle the packages the project use `pipenv`

```
$ pip install --user pipx
$ pipx install pipenv
```

```
$ cd /path-to-cv-generator
$ pipenv install
```

## Usage

First create a custom name subdirectory (like `sample`) inside of `/data` with the following structure:

```
data/
└── sample
    ├── data.js
    └── img
```

In `data.js` is where all your data cv will be stored. And inside `./data/sample/img` you can store the custom img that you need like your profile picture.


```
$ pipenv shell
(cv-generator)$ python main.py --help
```

```
$ pipenv shell
(cv-generator)$ python main.py sample
```



## References

- [Jinja2](https://jinja.palletsprojects.com/)
- [pipenv](https://pipenv.pypa.io/en/latest/)