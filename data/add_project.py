from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Project(name=random_string("name", 10))]