# Contentstack Utility

This guide will help you get started with Contentstack Python Utils SDK to build apps powered by Contentstack.

## Prerequisites

The latest version of [PyCharm](https://www.jetbrains.com/pycharm/download/) or [Visual Studio Code](https://code.visualstudio.com/download)

[Python 3](https://docs.python-guide.org/starting/installation/#python-3-installation-guides)

[Create virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

[Activate virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment)

## SDK Installation and Setup

### Install from PyPI

The package is published on PyPI as **`contentstack-utils`** (hyphen). Import it in Python as **`contentstack_utils`** (underscore):

```bash
pip install contentstack-utils
```

Runtime dependencies (including **`lxml`**, required for HTML rendering) are installed automatically.

### Install for local development

Clone the repository, create a virtual environment, then install the package in editable mode with dev tools (pytest, linters):

```bash
git clone https://github.com/contentstack/contentstack-utils-python.git
cd contentstack-utils-python
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

Alternatively, install the package and dev dependencies separately:

```bash
pip install -e .
pip install -r requirements.txt
```

### Run tests

```bash
pytest
```

Test discovery and defaults are configured in `pyproject.toml` under `[tool.pytest]`.

### Use with the Contentstack Python SDK

If you install the main Contentstack Python SDK, you may still need **`contentstack-utils`** separately depending on your SDK version and how dependencies are declared:

```bash
pip install contentstack
pip install contentstack-utils
```

## For the latest version

```bash
pip install contentstack
```

## For the specific version

```bash
pip install contentstack==1.5.1
```

## Usage

Let’s learn how you can use Utils SDK to render embedded items. 

### Create Render Option

To render embedded items on the front-end, use the renderContents function, and define the UI elements you want to show in the front-end of your website, as shown in the example code below:

```python
    from contentstack_utils.utils import Utils
    from contentstack_utils.render.options import Options
    
    json_array = {} # should be type of dictionary or list
    option = Options()
    response = Utils.render_content('html_string', json_array, option)
    print(response)
    
```

## Basic Queries

Contentstack Utils SDK lets you interact with the Content Delivery APIs and retrieve embedded items from the RTE field of an entry.

## Fetch Embedded Item(s) from a Single Entry

To get an embedded item of a single entry, you need to provide the stack API key, environment name, content type’s UID, and entry’s UID. Then, use the `entry.fetch` function as shown below:

```python
import contentstack
    
stack = contentstack.Stack('api_key','delivery_token','environment')
content_type = stack.content_type("content_type_uid")
entry = content_type.entry("entry_uid")
result = entry.fetch()
if result is not None:
   entry = result['entries']
   Utils.render(entry, ['rich_text_editor', 'some_other_text'], Option())
       
```

## Fetch Embedded Item(s) from Multiple Entries

To get embedded items from multiple entries, you need to provide the stack API key, delivery token, environment name, and content type’s UID. 

```python
import contentstack

stack = contentstack.Stack('api_key','delivery_token','environment')
query = stack.content_type("content_type_uid").query()
result = query.find()
if result is not None and 'entries' in result:
   entry = result['entries']
   for item in range:
       option = Option()
       Utils.render(item, ['rich_text_editor', 'some_other_text'], option)
```


## Supercharged

To get supercharged items from multiple entries, you need to provide the stack API key, delivery token, environment name, and content type’s UID. 

```python
import contentstack

stack = contentstack.Stack('api_key','delivery_token','environment')
query = stack.content_type("content_type_uid").query()
result = query.find()
if result is not None and 'entries' in result:
   entry = result['entries']
   for item in entry:
       option = Option()
       Utils.json_to_html(item, ['paragraph_text'], option)
```

## GraphQL SRTE

To get supercharged items from multiple entries, you need to provide the stack API key, delivery token, environment name, and content type’s UID. 

```python
import contentstack

stack = contentstack.Stack('api_key','delivery_token','environment')
query = stack.content_type("content_type_uid").query()
result = query.find()
if result is not None and 'entries' in result:
   entry = result['entries']
   for item in entry:
       option = Option()
       GQL.json_to_html(item, ['paragraph_text'], option)
```
