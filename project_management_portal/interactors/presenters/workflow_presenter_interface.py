from abc import ABC, abstractmethod
from typing import List
from project_management_portal.dtos import WorkflowDetailsDto

class WorkflowPresenterInterface(ABC):

    def get_workflows_response(
        self,
        workflow_details_dtos: List[WorkflowDetailsDto]
        ):

        pass
