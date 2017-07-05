from unittest.mock import patch

from tdd import datawrapper as dw


def test_init():
    dw.DataWrapper()


@patch('tdd.datawrapper.RestService')
def test_datawrapper_initializes_restservice(mock_restservice):
    dw.DataWrapper()

    assert mock_restservice.called


@patch('tdd.datawrapper.RestService')
def test_datawrapper_list_calls_list_method(mock_restservice):
    w = dw.DataWrapper()
    w.list()

    assert mock_restservice().list.called


@patch('tdd.datawrapper.RestService')
def test_datawrapper_list_returns_correct_data(mock_restservice):
    test_data = [
        {
            "id": 1,
            "name": "Laith",
            "surname": "Simmons",
            "age": 68,
            "salary": "£27888"
        },
        {
            "id": 2,
            "name": "Mikayla",
            "surname": "Henry",
            "age": 49,
            "salary": "£67137"
        },
        {
            "id": 3,
            "name": "Garth",
            "surname": "Fields",
            "age": 70,
            "salary": "£70472"
        },
    ]

    mock_restservice().list.return_value = test_data

    w = dw.DataWrapper()

    assert w.list() == test_data
