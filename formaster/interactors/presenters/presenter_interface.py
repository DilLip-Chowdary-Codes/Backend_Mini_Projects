from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def submit_form_response_return(self, response_id: int):
        pass

    @abstractmethod
    def raise_invalid_form_id(self):
        pass

    @abstractmethod
    def raise_form_closed(self):
        pass

    @abstractmethod
    def raise_invalid_question_id(self):
        pass

    @abstractmethod
    def raise_invalid_user_response(self):
        pass
