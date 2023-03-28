import pytest

from main import count_words, count_sentences


@pytest.fixture
def example_text():
    return "This is an example sentence. It has seven words!"


@pytest.mark.parametrize("text,expected", [
    ("This is a sentence.", 4),
    ("This is another sentence!", 3),
    ("A single-word sentence.", 1),
    ("This text\ncontains\nnewlines.", 3),
    ("", 0),
])
def test_count_words(text, expected):
    assert count_words(text) == expected


@pytest.mark.parametrize("text,expected", [
    ("This is a sentence.", 1),
    ("This is another sentence!", 1),
    ("A single-sentence text.", 1),
    ("This text\ncontains\nmultiple sentences.", 3),
    ("", 0),
])
def test_count_sentences(text, expected):
    assert count_sentences(text) == expected


def test_count_words_with_fixture(example_text):
    assert count_words(example_text) == 7


def test_count_sentences_with_fixture(example_text):
    assert count_sentences(example_text) == 2
