

def test_login(app):
    app.session.login("administrator", "roo")
    assert app.session.is_logged_in_as("administrator")