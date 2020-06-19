from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.form_submission import FormSubmission
from formaster.exceptions import InvalidUserResponse

class FillInTheBlanksFormSubmission(FormSubmission):

    def __init__(self, storage: StorageInterface, question_id: int,
                 form_id: int, user_id: int, user_submitted_text_answer: int):
        self.user_submitted_text_answer = user_submitted_text_answer
        super().__init__(storage, question_id, form_id, user_id)

    def validate_user_response(self):
        is_text_invalid = not self.user_submitted_text_answer
        if is_text_invalid:
            raise InvalidUserResponse()

    def create_user_response(self):
        response_id = self.storage.create_user_fill_in_the_blanks_response(
            self.user_id,
            self.form_id,
            self.question_id,
            self.user_submitted_text_answer)
        return response_id
