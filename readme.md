# Document Generator

Document Generator is a project to generate randomized documents based on content retrieved from Wikipedia with paraphrasing. The generated documents may be used in various instances, most notably for uploading to CourseHero as study materials.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

You will also need to download [nltk](https://www.nltk.org/) modules. The script `nltkdownload.py` will automatically download all the nltk packages you need.

The command below will install all dependencies in requirements.txt and install the modules from nltk

For MacOS:

```bash
python3 -m pip install -r requirements.txt && python3 nltkdownload.py
```

If there are issues installing `lxml` on MacOS the issue may be that xcode command tools is not installed. xcode command tools can be installed with the following command:

```bash
xcode-select --install
```

## Usage

When executed with no further arguments, the program will generate one batch of documents with randomized pages from Wikipedia.

```bash
usage: generate_documents.py [-h] [-t TITLE] [-n NUMBER] [-b BATCH]
                             [-c CLASS_NAMES] [-s SENTENCES]

optional arguments:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        The wikipedia page title to use for generating
                        documents (default: None)
  -n NUMBER, --number NUMBER
                        The number of documents to generate in a batch
                        (default: 10)
  -b BATCH, --batch BATCH
                        The number of batches to generate (default: 1)
  -c CLASS_NAMES, --class_names CLASS_NAMES
                        The class names to use for generating documents.
                        You should parenthesize the class name if it contains white spaces.
                        (default: ['CS 1', 'CS 2', 'CS 3', 'CS 4', 'CS 5', 'CS
                        6', 'CS 7', 'CS 8', 'CS 9', 'CS 10'])
  -s SENTENCES, --sentences SENTENCES
                        The number of sentences to use for each chunk
                        (default: 25)

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
