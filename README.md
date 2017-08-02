# htmltoapi
Python library to quickly convert an HTML page to a usable read-only JSON api.

Why use this? Good for hackathons or sometimes you just want to scrape a page into JSON without a lot of hassle

# Basic Usage

Getting started is pretty easy.

1. Identify the site you want to use for your read-only api. This tool works best on sites that content that flows linearly down a page - just for example : reddit.com
2. Make a configuration dictionary:
    ~~~
    config = {
        "resources": [
        ]
    }
    ~~~
3. Add "resources"
    ```
    config = {
        "resources": [
            {
                "name": "Article",
                "source_url": "http://www.burlingtonfreepress.com/news/local/",
                "elements": [
                    {
                        "name": "link",
                        "element": {
                            "type": "a",
                            "class": "hgpm-link",
                            "attribute": "href"
                        }
                    },
                    {
                        "name": "title",
                        "element": {
                            "type": "p",
                            "class": "hgpm-image-hed"
                        }
                    }
                ]
            }
        ]
    }
    ```
4. A resource is comprised of
    1. name - this is the name of your resource
    2. source_url - where to find the resource elements
    3. elements - This is an array of dictionaries that describe the html elements on the page
        1. Each element should be given a "name" which will appear in the json output
5. Pass the configuration to the serverbuilder.Builder() and call create()
    ```
    """Create the API Server"""
    serverbuilder.Builder(config).create()
    ```
6. A flask server will be generated in the /server directory. For the time being until I can get to it, move the file into the root directory and run it. You'll have a running flask server on localhost:5000 which you can use to GET your resources, for example if using the configuration above:

    GET localhost:5000/api/articles
    
    Would return:
    ```    
        {
            data: [
                {
                link: "/story/news/local/vermont/2017/07/24/fake-news-ask-librarian/489003001/",
                title: "Fake news? Ask a librarian"
                },
                {
                link: "/videos/news/2017/07/25/fake-news-schmake-news.-librarian-knows-difference/103966880/",
                title: "Fake news, schmake news. This librarian knows the difference"
                },
                {
                link: "/videos/life/2017/07/25/-your-garden-green/103994210/",
                title: "Is your garden green?"
                },
                {
                link: "/story/news/2017/07/25/interpretation-challenge-small-city/475206001/",
                title: "Drowning shines a light on Winooski's challenges"
                },
                {
                link: "/videos/news/2017/07/26/one-day-co-working-space-draws-entrepreneurs/104016058/",
                title: "One-day co-working space draws entrepreneurs"
                },
                {
                link: "/story/news/local/vermont/2017/07/26/btv-south-end-makeover-underway/512685001/",
                title: "BTV South End makeover under way"
                }
            ],
            name: "Article"
        }
    ```

