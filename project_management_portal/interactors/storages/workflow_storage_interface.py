from abc import ABC, abstractmethod

class WorkflowStorageInterface(ABC):
    def get_workflows(self):
        pass
