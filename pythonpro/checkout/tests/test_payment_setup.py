import pytest
from django_pagarme import facade
from django_pagarme.models import PagarmeFormConfig


def test_config_creation():
    assert PagarmeFormConfig.objects.count() == 2


@pytest.fixture
def first_pagarme_form_config():
    return PagarmeFormConfig.objects.order_by('id').first()


def test_first_config_properties(first_pagarme_form_config):
    assert (
               first_pagarme_form_config.name,
               first_pagarme_form_config.max_installments,
               first_pagarme_form_config.default_installment,
               first_pagarme_form_config.free_installment,
               first_pagarme_form_config.interest_rate,
               first_pagarme_form_config.payments_methods,
           ) == (
               'Boleto ou Cartão 12 vezes juros 1.66%',
               12,
               1,
               1,
               1.66,
               'credit_card,boleto'
           )


def test_item_config_pytools(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('pytools')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Curso Pytools',
               'pytools',
               39700,
               False,
               first_pagarme_form_config
           )


def test_item_config_pytools_oto(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('pytools-oto')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Curso Pytools 75 Off',
               'pytools-oto',
               9700,
               False,
               first_pagarme_form_config
           )


def test_item_config_pytools_done(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('pytools-done')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Curso Pytools 50 Off',
               'pytools-done',
               19850,
               False,
               first_pagarme_form_config
           )


def test_item_membership(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('membership')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Inscricão Turma Python Pro',
               'membership',
               199700,
               False,
               first_pagarme_form_config
           )


def test_item_membership_for_client(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('membership-client')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Inscricão Turma Python Pro 100 R Off',
               'membership-client',
               189700,
               False,
               first_pagarme_form_config
           )


def test_item_membership_for_client_first_day(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('membership-client-first-day')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Inscricão Turma Python Pro 500 R Off',
               'membership-client-first-day',
               149700,
               False,
               first_pagarme_form_config
           )


def test_item_membership_first_day(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('membership-first-day')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Inscricão Turma Python Pro 400 R Off',
               'membership-first-day',
               159700,
               False,
               first_pagarme_form_config
           )


def test_item_webdev_oto(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('webdev-oto')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Webdev Django 50% de Desconto',
               'webdev-oto',
               49700,
               False,
               first_pagarme_form_config
           )


def test_item_webdev(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('webdev')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Webdev Django',
               'webdev',
               99700,
               False,
               first_pagarme_form_config
           )


def test_item_data_science(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('data-science')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Ciência de Dados',
               'data-science',
               49700,
               False,
               first_pagarme_form_config
           )


@pytest.fixture
def second_pagarme_form_config():
    return PagarmeFormConfig.objects.order_by('id').all()[1]


def test_second_config_properties(second_pagarme_form_config):
    assert (
               second_pagarme_form_config.name,
               second_pagarme_form_config.max_installments,
               second_pagarme_form_config.default_installment,
               second_pagarme_form_config.free_installment,
               second_pagarme_form_config.interest_rate,
               second_pagarme_form_config.payments_methods,
           ) == (
               'Cartão 12 vezes juros 1.66%',
               12,
               1,
               1,
               1.66,
               'credit_card'
           )


def test_item_bootcamp(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('bootcamp')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Bootcamp Python Pro',
               'bootcamp',
               199700,
               False,
               first_pagarme_form_config
           )


def test_item_bootcamp_35_discount(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('bootcamp-35-discount')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Bootcamp Python Pro - 35% de Desconto',
               'bootcamp-35-discount',
               129700,
               False,
               first_pagarme_form_config
           )


def test_item_bootcamp_50_discount(second_pagarme_form_config):
    item_config = facade.find_payment_item_config('bootcamp-50-discount')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Bootcamp Python Pro - 50% de Desconto',
               'bootcamp-50-discount',
               99700,
               False,
               second_pagarme_form_config
           )


def test_item_bootcamp_webdev(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('bootcamp-webdev')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Bootcamp Python Pro - R$497 Off',
               'bootcamp-webdev',
               150000,
               False,
               first_pagarme_form_config
           )


def test_item_bootcamp_webdev_35_discount(first_pagarme_form_config):
    item_config = facade.find_payment_item_config('bootcamp-webdev-35-discount')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Bootcamp Python Pro - 35% de Desconto - R$497 Off',
               'bootcamp-webdev-35-discount',
               80000,
               False,
               first_pagarme_form_config
           )


def test_item_bootcamp_webdev_50_discount(second_pagarme_form_config):
    item_config = facade.find_payment_item_config('bootcamp-webdev-50-discount')
    assert (
               item_config.name,
               item_config.slug,
               item_config.price,
               item_config.tangible,
               item_config.default_config,
           ) == (
               'Bootcamp Python Pro - 50% de Desconto - R$497 Off',
               'bootcamp-webdev-50-discount',
               50000,
               False,
               second_pagarme_form_config
           )
