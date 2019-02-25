from combined.semyon.builders import Director, TextClassifierBuilder


if __name__ == '__main__':

    director = Director()
    builder = TextClassifierBuilder()
    director.builder = builder

    director.build_baseline_classifier()

    text = 'That is an interesting movie with good actors. I would recommend it for sure'

    print(director.builder.classifier.eval([text]))

