import pytest

from django.urls import reverse


@pytest.fixture
def resp(client_with_lead, db):
    return client_with_lead.get(reverse('checkout:webdev_landing_page'))


def test_should_page_exists(resp):
    assert resp.status_code == 200
