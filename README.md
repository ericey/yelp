# Yelp

## Getting Started

You'll need [Python 3](https://www.python.org/downloads/) and
[Node.js](https://nodejs.org/en/download/) to run the code in this
project.

### Reviews

The review fetching script is written in Node.js and uses Google
Chrome's [Puppeteer](https://github.com/GoogleChrome/puppeteer). First,
install all of the Node dependencies.

```bash
    $ npm install
```

Now you can fetch reviews. If the URL for a business is
`https://www.yelp.com/biz/tartine-bakery-and-cafe-san-francisco`, then
`tartine-bakery-and-cafe-san-francisco` is the business id. Pass this
into `/bin/reviews` to get all the reviews for the business in JSON
format.

```bash
    $ ./bin/reviews tartine-bakery-and-cafe-san-francisco
```
