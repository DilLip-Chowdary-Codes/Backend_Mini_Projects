from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.form_submission import FormSubmission
from formaster.exceptions import InvalidUserResponse

class MCQsFormSubmission(FormSubmission):

    def __init__(self, storage: StorageInterface, question_id: int,
                 form_id: int, user_id: int, user_submitted_option_id: int):
        self.user_submitted_option_id = user_submitted_option_id
        super().__init__(storage, question_id, form_id, user_id)

    def validate_user_response(self):

        option_ids = self.storage.get_option_ids_for_question(self.question_id)
        if self.user_submitted_option_id not in option_ids:
            raise InvalidUserResponse()

    def create_user_response(self):
        response_id = self.storage.create_user_mcq_response(
            self.user_id,
            self.form_id,
            self.question_id,
            self.user_submitted_option_id)
        return response_id
