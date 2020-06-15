from abc import ABC
from abc import abstractmethod
from typing import List
from project_management_portal.dtos\
    import TaskDto, TaskDetailsDto, TransitionDto, StateDto

class TaskStorageInterface(ABC):

    @abstractmethod
    def validate_state_id(self, state_id: int) -> bool:
        pass

    @abstractmethod
    def validate_task_id(self, task_id: int) -> bool:
        pass

    @abstractmethod
    def create_task(self, user_id: int, task_dto: TaskDto):
        pass

    @abstractmethod
    def get_tasks(self, project_id: int) -> List[TaskDetailsDto]:
        pass

    @abstractmethod
    def update_task_state(
        self,
        task_id: int,
        updated_state_id: int,
        satisfied_checkpoints_ids: List[int]
        ) -> TaskDetailsDto:

        pass
    
    @abstractmethod
    def get_states_for_task_based_on_current_state(
        self,
        task_id: int,
        current_state_id: int) -> List[StateDto]:

        pass
