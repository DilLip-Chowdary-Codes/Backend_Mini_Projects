from abc import ABC
from abc import abstractmethod

class TaskPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_state_id_exception(self):
        pass

    @abstractmethod
    def raise_invalid_task_id_exception(self):
        pass

    @abstractmethod
    def get_task_details_response(self, task_details_dto):
        pass

    @abstractmethod
    def get_create_task_response(self, task_details_dto):
        pass

    @abstractmethod
    def get_tasks_response(self, tasks_details_dtos):
        pass
    
    @abstractmethod
    def get_task_states_response(self, states_dtos):
        pass

