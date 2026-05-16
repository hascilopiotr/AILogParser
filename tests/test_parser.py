import pytest
from src.parse import LogParser
from pytest import fixture

@pytest.fixture
def parser():
    return LogParser()

def wrong_timestamp(parser):
    line = '23122004 [ERROR] [db]'
    result = parser.parse_line(line)
    assert result['timestamp'] == '2004-12-23 [ERROR] [db]'
    assert result['level'] == 'ERROR'
    assert result['message'] == '[ERROR] [db]'



def test_parser_line_valid(parser):
    line = '[2025-01-01 08:00:07] [INFO] [auth] User login successful'
    result = parser.parse_line(line)

    assert result is not None
    assert result['level'] == 'INFO'
    assert result['message'] == 'User login successful'
    assert result['module'] == 'auth'

def test_not_valid_line(parser):
    line = 'to nie jet log'
    result = parser.parse_line(line)

    assert result is None

def test_empty_string(parser):
    line = ''
    result = parser.parse_line(line)
    assert result is None

def test_parse_line_handles_special_chars_in_message(parser):
    line = '[2025-01-01 08:00:07] [ERROR] [db] Query failed: SELECT * FROM users WHERE id = 42'

    result = parser.parse_line(line)

    assert result['message'] == 'Query failed: SELECT * FROM users WHERE id = 42'

