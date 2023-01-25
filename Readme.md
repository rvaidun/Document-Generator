# Document Generator

Document Generator is a Python3 script to automatically generate documents. This project works by paraphrasing existing wikipedia articles and writing the paraphrased text to a word document that you can upload to coursehero. These documents can be used for various purposes including uploading to Coursehero.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.


You will also need to download [nltk](https://www.nltk.org/) modules. The script `nltkdownload.py` will automatically download all the nltk packages you need.


The command below will install all dependencies in requirements.txt and install the modules from nltk
```bash
pip install -r requirements.txt && python3 nltkdownload.py
```
## Usage

![demo](https://github.com/rvaidun/Document-Generator/raw/master/demo.gif)

```python
python3 generate_documents.py [NUMBER_OF_DOCUMENTS: INTEGER] [WIKIPEDIA_ARTICLE_TITLE]
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
