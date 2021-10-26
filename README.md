# `About`
A basic wikipedia scraper which grabs information from wikipedia.org based on user input.
> Made by Advait Jadhav!

# `Depends On`
- wikipedia==1.4.0
- click==8.0.3
- rich==10.12.0

# `Installation`
1. Download or clone the repository.

2. Open command-line window in the directory containing this repository.

3. Run the command below on command-line.

```pip install -r requirements.txt```

4. Once the dependencies are installed run the command below.

```python setup.py install```

5. Now, you can call the `wikiscraper` command from any location on your machine.

# `A simple example`

```
$ wikiscraper fetch
Enter the query for your wikipedia search: India
    India, officially the Republic of India (Hindi: Bhārat Gaṇarājya), is a country in South Asia. It is the seventh-largest country by area, the second-most populous country, and the most populous democracy in the world.
```

#### We can even specify the number of sentences and language
```
$ wikiscraper fetch --help
Usage: wikiscraper fetch [OPTIONS]

  fetches and displays information based on the query passed in.

Options:
  -q, --query TEXT         Query for wikipedia search!
  -s, --sentences INTEGER  Number of sentences to be displayed.
  -l, --lang TEXT          Language in which the information will be
                           displayed.
  --help                   Show this message and exit.
```
