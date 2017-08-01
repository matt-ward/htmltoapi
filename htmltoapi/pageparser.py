from bs4 import BeautifulSoup

class Parser:

    def __init__(self, config, page):

        self.config = config
        self.page = page

    def parse(self):

        soup = BeautifulSoup(self.page, "lxml")

        elements = self.config.get('elements', None)

        element_answers = []
        for element in elements:

            element_type = element['element']['type']
            element_class = element['element']['class']
            element_attribute = element['element'].get('attribute', None)

            if element_attribute is not None:

                answers = map(lambda x: {element['name']: x[element_attribute]},
                              soup.findAll(element_type, class_=element_class))
            else:
                answers = map(lambda x: {element['name']: x.get_text()},
                              soup.findAll(element_type, class_=element_class))

            element_answers.append(answers)

        return Parser.__make_collections(element_answers)

    @staticmethod
    def __make_collections(element_answers):

        final = []
        items = 2
        while items > 1:

            collection = []

            for group in element_answers:
                items = len(group)

                collection.append(group.pop())

            final.append({k: v for d in collection for k, v in d.items()})

        return final

