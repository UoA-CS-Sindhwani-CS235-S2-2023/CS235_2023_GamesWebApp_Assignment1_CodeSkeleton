import pytest
from games.domainmodel.model import Publisher, Genre, Game, Review, User, Wishlist


class TestArtist:

    def test_construction(self):
        publisher1 = Publisher("Publisher A")
        assert str(publisher1) == "<Publisher Publisher A>"
        publisher2 = Publisher("Publisher B")
        assert str(publisher2) == "<Publisher Publisher B>"
        publisher3 = Publisher("Publisher C")
        assert str(publisher3) == "<Publisher Publisher C>"

        # TODO - the test will fail as the code is incomplete......

# TODO
