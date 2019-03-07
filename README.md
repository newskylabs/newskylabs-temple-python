
# Templates for a NewSkyLabs python project


## {{ company.name }} {{ project.language }} project {{ project.name }}

Use [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to format the content of this file.

For more information concerning the used template syntax see the
[homepage of *Jinja2*](http://jinja.pocoo.org/docs/).


## Project settings

* project name:  {{ project.name }}
* author:        {{ author.name }}
* homepage:      {{ author.homepage }}
* email:         {{ author.email }}
* contact:       {{ author.contact }}
* company:       {{ company.name }}
* date:          {{ date }}
* copyright:     {{ copyright }}

## Usage

1. Install [NewSkyLab](http://newskylabs.net/)'s template generator
[temple](https://github.com/newskylabs/newskylabs-temple)

You can install *temple* with *pip* directly from its *[github
repository](https://github.com/newskylabs/newskylabs-temple)*:

```sh
pip install git+https://github.com/newskylabs/newskylabs-temple
```

2. Download the templates:

```sh
git clone https://github.com/newskylabs/newskylabs-temple-python
```


3. Create a *temple* settings file:

```sh
mkdir -p ~/.newskylabs/temple

cat > ~/.newskylabs/temple/settings.yaml <<FIN
## temple's setting file

author:
  first-name: Your
  family-name: Name
  email: your@email.address

company: 
  name: YourCompany

version: 1.0.0
status: Production
license: MIT

python-project:
  language: Python
  template-dir: newskylabs-temple-python
  project-dir: .

FIN

```

4. Use *temple* to generate a file directory tree corresponding to the
template hierarchy:

```sh
temple generate python-project my-project
```

4. Have a look on the result:

```sh
$ find my-project
my-project
my-project/my-project.git
my-project/my-project.git/LICENSE
my-project/my-project.git/newskylabs
my-project/my-project.git/newskylabs/temple
my-project/my-project.git/newskylabs/temple/__init__.py
my-project/my-project.git/newskylabs/temple/__about__.py
my-project/my-project.git/README.md
my-project/my-project.git/setup.py
my-project/my-project.git/.gitignore

$ tail -10 my-project/my-project.git/README.md

## Project settings

* project name:  my-project
* author:        Your Name
* homepage:      http://your.home.page/
* email:         your@email.address
* contact:       http://your.home.page/contact
* company:       YourCompany
* date:          2019/03/04
* copyright:     Copyright 2019 Your Name

```

# Comments etc.

If you have any comments, [please drop me a message]({{ author.contact }})!

*Copyright (c) {{ datetime.year }} [{{ author.name }}]({{ author.homepage }})*
