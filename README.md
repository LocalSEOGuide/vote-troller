# LSG Vote Troller
This is a simple selenium based script to blast voting pages. 

## Installation
`pip install -r requirements.txt`

## Config
Create a file called `config.py`. It should look like this example, but replace the values with your own.

```python
"""Configuration file."""

# The URL of the poll
poll_url = 'https://www.example.com/poll'

# The names of the nominees to vote for
# These should match the names listed on the poll exactly
names = [
    'Captain SEO',
    'John Smith',
    'Jane Doe',
    'Mr Nobody'
]

# The proxy connection strings
http_proxy_string = 'https://<username>:<password>@proxy.example.com:<port>'
https_proxy_string = 'https://<username>:<password>@proxy.example.com:<port>'

# The selector of the root element that contains the name of the nominee and
# the button to click to vote for them.
# Note that "NAME" here will be replaced with a name from your list of names
# (see above)
root_element_xpath = (
    '//div[contains(@class, "seo_expert-item")][contains(., "NAME")]'
)

# The sub-xpath that specifies the button to click to vote for the nominee
# This xpath will be applied from within the root_element_xpath
button_xpath = '//*[contains(@class, "likebtn-button")]'

# Number of times to vote
num_of_votes = 50
```

## Usage
`python vote-troller.py`
