import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(123, 'victor')
        encrypt_message('victor', 1.5)
    assert encrypt_message('victor', 7) == 'rotciv'
    assert encrypt_message('victor', -1) == 'rotciv'
    assert encrypt_message('matheus', 6) == 's_uehtam'
    assert encrypt_message('matheus', 5) == 'ehtam_su'
