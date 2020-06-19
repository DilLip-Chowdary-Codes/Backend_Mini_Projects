from abc import abstractmethod

from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface\
    import PresenterInterface
from formaster.exceptions import FormClosed, InvalidFormId,\
                                 InvalidQuestionId, InvalidUserResponse

class FormSubmission:

    def __init__(self, storage: StorageInterface,
                 question_id: int, form_id: int, user_id: int):
        self.storage = storage
        self.question_id = question_id
        self.form_id = form_id
        self.user_id = user_id

    def form_submission_wrapper(self, presenter: PresenterInterface):
        try:
            response_id = self.form_submission(self.question_id,
                                               self.form_id,
                                               self.user_id)
        except InvalidFormId:
            presenter.raise_invalid_form_id()
        except FormClosed:
            presenter.raise_form_closed()
        except InvalidQuestionId:
            presenter.raise_invalid_question_id()
        except InvalidUserResponse:
            presenter.raise_invalid_user_response()
        response = presenter.submit_form_response_return(response_id)
        print(response)
        return response

    def form_submission(self, question_id: int,
                        form_id: int, user_id: int):
        form_dto = self.storage.get_form(form_id)
        is_form_closed = not form_dto.is_live
        if is_form_closed:
            raise FormClosed()

        self.storage.validate_question_id_with_form(self.question_id,
                                                    self.form_id)
        self.validate_user_response()
        return self.create_user_response()

    @abstractmethod
    def validate_user_response(self):
        pass

    @abstractmethod
    def create_user_response(self):
        pass
