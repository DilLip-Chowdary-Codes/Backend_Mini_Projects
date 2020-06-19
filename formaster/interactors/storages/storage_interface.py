from abc import ABC, abstractmethod

class StorageInterface(ABC):
    @abstractmethod
    def get_form(self, form_id):
        pass

    @abstractmethod
    def validate_question_id_with_form(self, question_id, form_id):
        pass

    @abstractmethod
    def get_option_ids_for_question(self, question_id):
        pass

    @abstractmethod
    def create_user_mcq_response(self, user_id, form_id, 
                                 question_id, user_submitted_option_id):
        pass

    @abstractmethod
    def create_user_fill_in_the_blanks_response(self, user_id, form_id, 
                                                question_id,
                                                user_submitted_text_answer):
        pass
