import pytest
from unittest.mock import Mock, create_autospec

from django_swagger_utils.drf_server.exceptions import BadRequest, Forbidden
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface\
    import PresenterInterface
from formaster.interactors.form_submission import FormSubmission
from formaster.exceptions import FormClosed, InvalidFormId,\
                                 InvalidQuestionId, InvalidUserResponse

class TestFormSubmission:

    def test_form_submission_with_invalid_form_id_raises_exception(self):
        #arrange
        question_id = 1
        form_id = 1
        user_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = FormSubmission(storage, question_id, form_id, user_id)
        storage.get_form.side_effect = InvalidFormId
        presenter.raise_invalid_form_id.side_effect = BadRequest

        #act
        with pytest.raises(BadRequest):
            interactor.form_submission_wrapper(presenter)

        #assert
        storage.get_form.assert_called_once_with(form_id)
        presenter.raise_invalid_form_id.assert_called_once()

    def test_form_submission_when_form_is_not_live_raises_exception(self,
                                                                    form_dto_not_live):
        #arrange
        question_id = 1
        form_id = 1
        user_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = FormSubmission(storage, question_id, form_id, user_id)
        storage.get_form.return_value = form_dto_not_live
        presenter.raise_form_closed.side_effect = Forbidden

        #act
        with pytest.raises(Forbidden):
            interactor.form_submission_wrapper(presenter)

        #assert
        storage.get_form.assert_called_once_with(form_id)
        presenter.raise_form_closed.assert_called_once()

    def test_form_submission_with_invalid_question_id_raises_exception(self,
                                                                    form_dto):
        #arrange
        question_id = 1
        form_id = 1
        user_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = FormSubmission(storage, question_id, form_id, user_id)
        storage.get_form.return_value = form_dto
        storage.validate_question_id_with_form.side_effect = InvalidQuestionId
        presenter.raise_invalid_question_id.side_effect = BadRequest

        #act
        with pytest.raises(BadRequest):
            interactor.form_submission_wrapper(presenter)

        #assert
        storage.get_form.assert_called_once_with(form_id)
        storage.validate_question_id_with_form.assert_called_once_with(
            question_id, form_id)
        presenter.raise_invalid_question_id.assert_called_once()
