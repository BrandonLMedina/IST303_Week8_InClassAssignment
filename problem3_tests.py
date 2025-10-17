import pytest
import time
import random
import problem3_code

# Test send_msg Function

# Test send_msg is returning a valid ID and storing the message
@pytest.mark.parametrize(
        "msg, delay, units",
          [("Test1", 5, "seconds"),
           ("Test2", 15, "seconds"),
           ("Test3", 30, "seconds")])

def test_send_msg(msg, delay, units):
    msg_id = problem3_code.send_msg(msg, delay, units)
    assert isinstance(msg_id, int),
    assert 100000 <= msg_id <= 999999,
    assert msg_id in problem3_code.message_dict,

# Test send_msg with invalid delay values
@pytest.mark.parametrize(
    "msg, delay, units",
    [("Delay1", "5", "seconds"),
     ("Delay2", 3.5, "seconds"),
     ("Delay3", [10], "seconds")])

def test_send_msg_invalid_delay(msg, delay, units):
    with pytest.raises(Exception):
        problem3_code.send_msg(msg, delay, units)

# Test send_msg with invalid units
@pytest.mark.parametrize(
    "msg, delay, units",
    [("BadUnit1", 5, "days"),
     ("BadUnit2", 10, "weeks"),
     ("BadUnit3", 15, "milliseconds")])

def test_send_msg_invalid_units(msg, delay, units):
    with pytest.raises(Exception):
        problem3_code.send_msg(msg, delay, units)

# Test get_msg function

# Test get_msg function before delay has passed
@pytest.mark.parametrize(
    "msg, delay, units",
    [("Early1", 10, "seconds")])

def test_get_msg_before_delay(msg, delay, units, capsys):
    msg_id = problem3_code.send_msg(msg, delay, units)
    result = problem3_code.get_msg(msg_id)
    captured = capsys.readouterr()
    assert result is False,
    assert "cannot retrieve your message" in captured.out.lower()

# Test get_msg function after delay has passed
@pytest.mark.parametrize(
    "msg, delay, units",
    [("UnlockedMsg", 1, "seconds")])

def test_get_msg_after_unlock(msg, delay, units, capsys):
    msg_id = problem3_code.send_msg(msg, delay, units)
    time.sleep(2)  # Wait for the message to unlock
    result = problem3_code.get_msg(msg_id)
    captured = capsys.readouterr()
    assert result is True,
    assert msg in captured.out

# Test get_msg with invalid message ID, no parametrization needed
def test_get_msg_invalid_id(capsys):
    invalid_id = random.randint(100000, 999999)
    while invalid_id in problem3_code.message_dict:
        invalid_id = random.randint(100000, 999999)
    result = problem3_code.get_msg(invalid_id)
    captured = capsys.readouterr()
    assert result is False,
    assert "no message found" in captured.out.lower()