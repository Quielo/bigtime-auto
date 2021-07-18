import pytest

import bot.objects as o
import bot.login as l
import bot.hours as h

# Objects
lists = o.selectLists
week = o.week
save = o.save


@pytest.fixture()
def setup_run():
    l.login()
    h.hours()

@pytest.fixture()
def setup_brakeout():
    pass


@pytest.mark.usefixtures("setup_run")
def test_mon():
    expected = "8.00"

    assert expected == h.monday, "Monday not passed"

def test_tue():
    expected = "8.00"

    assert expected == h.tuesday, "Tuesday not passed"

def test_wed():
    expected = "8.00"

    assert expected == h.wednesday, "Wednesday not passed"

def test_thu():
    expected = "8.00"

    assert expected == h.thursday, "Thursday not passed"

def test_fri():
    expected = "8.00"

    assert expected == h.friday, "Friday not passed"

