class Publisher:
    def __init__(self, publisher_name: str):
        self.__publisher_name = None
        # TODO
        pass

    @property
    def publisher_name(self) -> str:
        return self.__publisher_name

    @publisher_name.setter
    def publisher_name(self, new_publisher_name: str):
        # TODO
        pass

    def __repr__(self):
        # we use access via the property here
        return f"<Publisher {self.__publisher_name}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__publisher_name == other.publisher_name

    def __lt__(self, other):
        # TODO
        pass

    def __hash__(self):
        # TODO
        pass


class Genre:
    # TODO
    pass


class Game:
    # TODO
    pass


class User:
    # TODO
    pass


class Review:
    # TODO
    pass


class Wishlist:
    # TODO
    pass
