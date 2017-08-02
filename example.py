from htmltoapi import serverbuilder

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


"""Create the API Server"""
serverbuilder.Builder(config).create()
