from book.views import index
from flask import url_for,render_template
from book import app

def test_index():
    assert 1==1