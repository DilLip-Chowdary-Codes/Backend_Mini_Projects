from typing import List
from django.db.models import F, Prefetch

from project_management_portal.interactors.storages.task_storage_interface\
    import TaskStorageInterface
from project_management_portal.dtos\
    import TaskDto, TaskDetailsDto,\
           TransitionDto, StateDto,\
           StateDetailsDto, TransitionDetailsDto,\
           ChecklistDetailsDto

from project_management_portal.models\
    import Project, State, Task, Workflow, Transition, Checklist

from project_management_portal.storages.project_storage_implementation\
        import ProjectStorageImplementation
from project_management_portal.adapters.service_adapter\
    import get_service_adapter

class TaskStorageImplementation(TaskStorageInterface):

    def validate_state_id(self, state_id: int) -> bool:
        is_state_valid = State.objects.filter(id=state_id).exists()
        return is_state_valid

    def validate_task_id(self, task_id: int) -> object:
        task = Task.objects.filter(id=task_id).first()
        task_exists = task

        if task_exists:
            task_dto = self._convert_task_obj_to_dto(task)
        else:
            task_dto = None

        return task_dto

    def create_task(self, user_id: int, task_dto: TaskDto):
        task = Task.objects.create(
            project_id=task_dto.project_id,
            issue_type=task_dto.issue_type,
            title=task_dto.title,
            assignee_id=user_id,
            description=task_dto.description,
            state_id=task_dto.state_id
            )

        task_details_dto = self._convert_task_obj_to_task_details_dto(task)
        return task_details_dto

    def get_tasks(self, project_id: int) -> List[TaskDetailsDto]:

        transition_set = Transition.objects\
            .select_related('from_state', 'to_state')

        workflow = Workflow.objects.prefetch_related(
            Prefetch('states'),
            Prefetch('transitions', queryset=transition_set)
            )

        project = Project.objects\
            .prefetch_related(
                Prefetch('workflow', queryset=workflow)
                )

        tasks = Task.objects\
            .select_related('state')\
            .prefetch_related(
                Prefetch('project', queryset=project))\
            .filter(project_id=project_id)\
            .order_by('-created_at')
        tasks_details_dtos = [
            self._convert_task_obj_to_task_details_dto(task)
            for task in tasks
            ]
        return tasks_details_dtos

    def update_task_state(
        self,
        task_id: int,
        updated_state_id: int,
        satisfied_checkpoints_ids: List[int]
        ) -> TaskDetailsDto:

        task_obj = Task.objects.get(id=task_id)
        task_obj.state_id = updated_state_id
        checkpoints_satisfied = Checklist.objects.filter(
            id__in=satisfied_checkpoints_ids)
        task_obj.conditions_satisfied.set(checkpoints_satisfied)
        task_obj.save()
        task_details_dto = self._convert_task_obj_to_task_details_dto(
            task_obj)

        return task_details_dto

    def get_states_for_task_based_on_current_state(
        self,
        task_id: int,
        current_state_id: int) -> List[StateDto]:

        transitions = Transition.objects\
            .select_related('from_state', 'to_state')\
            .prefetch_related('checklist')\
            .filter(workflow__project__task__id=task_id,
                    from_state_id=current_state_id)

        available_states_dtos = [
            self._convert_state_obj_to_state_details_dto(transition.to_state)
            for transition in transitions
            ]

        return available_states_dtos

    @staticmethod
    def _convert_task_obj_to_task_details_dto(task_obj):
        project_utils = ProjectStorageImplementation()
        projec_details_dto = project_utils\
            ._convert_project_object_to_project_details_dto(task_obj.project)
        adapter_service = get_service_adapter()
        user_service = adapter_service.user_service

        user_details_dto = user_service.get_user_dto(task_obj.assignee_id)

        task_details_dto = TaskDetailsDto(
            task_id=task_obj.id,
            project=projec_details_dto,
            issue_type=task_obj.issue_type,
            title=task_obj.title,
            assignee_id=user_details_dto,
            description=task_obj.description,
            state=task_obj.state.name
            )
        return task_details_dto

    @staticmethod
    def _convert_task_obj_to_dto(task_obj):

        task_dto = TaskDto(
            project_id=task_obj.project_id,
            issue_type=task_obj.issue_type,
            title=task_obj.title,
            description=task_obj.description,
            state_id=task_obj.state_id
            )
        return task_dto

    @staticmethod
    def _convert_state_obj_to_state_details_dto(state):

        state_details_dto = StateDetailsDto(
            state_id=state.id,
            name=state.name
            )

        return state_details_dto
