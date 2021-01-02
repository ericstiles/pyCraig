class Effect(object):
    pass


class Result:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def a(self):
        pass

    def bind(self, effect: Effect, effect_str: Effect):
        pass


class Failure(Result):
    def __init__(self):
        pass

    def __str__(self):
        pass


class Success(Result):
    def __init__(self):
        pass

    def __str__(self):
        pass
