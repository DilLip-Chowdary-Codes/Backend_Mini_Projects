import pytest
from formaster.interactors.storages.dtos import FormDto

@pytest.fixture()
def form_dto():
    form_dto = FormDto(
        form_id=1,
        title="Form",
        is_live=True
        )
    return form_dto

@pytest.fixture()
def form_dto_not_live():
    form_dto = FormDto(
        form_id=1,
        title="Form",
        is_live=False
        )
    return form_dto

@pytest.fixture()
def mcq_response():
    mcq_response = {
        "id":2
    }
    return mcq_response

@pytest.fixture()
def fill_in_the_blank_response():
    fill_in_the_blank_response = {
        "id":2
    }
    return fill_in_the_blank_response
