import json
import pytest
from parser import parser_log

def test_top_ip(tmp_path):
    log = tmp_path / "test.log"
    log.write_text(
        '192.168.1.1 - - [14/Jun/2026:10:00:01 +0000] "GET / HTTP/1.1" 200 1234 0.100\n'
        '192.168.1.1 - - [14/Jun/2026:10:00:02 +0000] "GET / HTTP/1.1" 200 1234 0.200\n'
        '192.168.1.2 - - [14/Jun/2026:10:00:03 +0000] "GET / HTTP/1.1" 200 1234 0.300\n'
    )
    counter, _ = parser_log(str(log))
    assert counter.most_common(1)[0][0] == "192.168.1.1"

def test_avg_response_time(tmp_path):
    log = tmp_path / "test.log"
    log.write_text(
        '192.168.1.1 - - [14/Jun/2026:10:00:01 +0000] "GET / HTTP/1.1" 200 1234 0.100\n'
        '192.168.1.2 - - [14/Jun/2026:10:00:02 +0000] "GET / HTTP/1.1" 200 1234 0.300\n'
    )
    _, times = parser_log(str(log))
    avg = sum(times) / len(times)
    assert avg == pytest.approx(0.200)

def test_empty_file(tmp_path):
    log = tmp_path / "test.log"
    log.write_text("")
    counter, times = parser_log(str(log))
    assert len(counter) == 0
    assert len(times) == 0