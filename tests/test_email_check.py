from app.modules.email_check import check_email


def test_invalid_format():
    result = check_email("not-an-email")
    assert result["valid_format"] is False


def test_valid_format():
    result = check_email("user@example.com")
    assert result["valid_format"] is True
