# test_doctests
import pytest  # noqa
import doctest

import nlpia_bot.clibot

import nlpia_bot.skills.eliza_bots
import nlpia_bot.skills.glossary_bots
import nlpia_bot.skills.qa_bots

import nlpia_bot.etl.glossaries
import nlpia_bot.etl.scrape_wikipedia
import nlpia_bot.etl.yml
import nlpia_bot.etl.elastic

import nlpia_bot.scores.semantics_score
# import nlpia_bot.template_generators


__author__ = "SEE AUTHORS.md"
__copyright__ = "Hobson Lane"
__license__ = "The Hippocratic License, see LICENSE.txt (MIT + Do no Harm)"

DOCTEST_KWARGS = dict(
    optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE,
    verbose=True)


def test_eliza_bots():
    results = doctest.testmod(nlpia_bot.skills.eliza_bots, **DOCTEST_KWARGS)
    assert results.failed < 1
    assert results.attempted > 0


def test_clibot():
    results = doctest.testmod(nlpia_bot.clibot, **DOCTEST_KWARGS)
    assert results.failed < 1
    assert results.attempted > 0


def test_glossaries():
    results = doctest.testmod(nlpia_bot.etl.glossaries, **DOCTEST_KWARGS)
    assert results.failed < 1
    assert results.attempted > 4


def test_qa_bots():
    results = doctest.testmod(nlpia_bot.skills.qa_bots, **DOCTEST_KWARGS)
    assert results.failed < 1
    assert results.attempted > 0


def test_scrape_wikipedia():
    results = doctest.testmod(nlpia_bot.etl.scrape_wikipedia, **DOCTEST_KWARGS)
    assert results.failed < 1
    assert results.attempted > 2

# def test_yml():
#     results = doctest.testmod(nlpia_bot.etl.yml, optionflags=doctest.ELLIPSIS |
#                               doctest.NORMALIZE_WHITESPACE, verbose=True)
#     assert results.failed < 1
#     assert results.attempted > 2


def test_semantics_score():
    results = doctest.testmod(nlpia_bot.scores.semantics_score, **DOCTEST_KWARGS)
    assert results.failed < 1
    assert results.attempted >= 1


# def test_template_generators():
#     results = doctest.testmod(nlpia_bot.template_generators, **DOCTEST_KWARGS)
#     assert results.failed < 1
#     assert results.attempted >= 1


def test_glossary_bots():
    results = doctest.testmod(nlpia_bot.skills.glossary_bots, **DOCTEST_KWARGS)
    assert results.failed < 1
    assert results.attempted > 2


def test_etl_elastic():
    results = doctest.testmod(nlpia_bot.etl.elastic, **DOCTEST_KWARGS)
    assert results.failed == 0
    assert results.attempted > 0
