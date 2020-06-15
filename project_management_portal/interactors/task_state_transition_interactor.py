from typing import Dict

#storages
from project_management_portal\
    .interactors.storages.task_storage_interface\
    import TaskStorageInterface
from project_management_portal\
    .interactors.storages.project_storage_interface\
    import ProjectStorageInterface
#presenters
from project_management_portal\
    .interactors.presenters.project_presenter_interface\
    import ProjectPresenterInterface
from project_management_portal\
    .interactors.presenters.task_presenter_interface\
    import TaskPresenterInterface

from project_management_portal.dtos\
    import TransitionDto, ChecklistStatusDto, UpdateTransitionInputDto

class TaskStateTransitionInteractor:

    def __init__(self,
                 project_storage: ProjectStorageInterface,
                 task_storage: TaskStorageInterface,
                 project_presenter: ProjectPresenterInterface,
                 task_presenter: TaskPresenterInterface):

        self.project_storage = project_storage
        self.task_storage = task_storage
        self.project_presenter = project_presenter
        self.task_presenter = task_presenter

    def update_task_state(self,
                        update_task_state_input_data: Dict):

        project_id = update_task_state_input_data['project_id']
        task_id = update_task_state_input_data['task_id']

        project_dto = self.project_storage.validate_project_id(
            project_id)
        is_project_invalid = not project_dto

        if is_project_invalid:
            self.project_presenter.raise_invalid_project_id_exception()

        task_dto = self.task_storage.validate_task_id(task_id=task_id)

        is_task_invalid = not task_dto
        if is_task_invalid:
            self.task_presenter.raise_invalid_task_id_exception()

        from_state_id = task_dto.state_id
        update_task_state_query_dto = self\
            ._convert_update_task_state_input_data_to_dto(
                update_task_state_input_data, from_state_id)

        to_state_id = update_task_state_query_dto.to_state_id

        workflow_id = project_dto.workflow_id
        is_transition_invalid = not self.project_storage\
            .validate_state_transition(
                workflow_id, from_state_id, to_state_id)

        if is_transition_invalid:
            self.project_presenter.raise_invalid_transition_exception()


        mandatory_checklist_dtos = self.project_storage\
            .get_transition_mandatory_checklist(update_task_state_query_dto)

        checklist_status_dtos = update_task_state_query_dto.checklist
        is_mandatory_checklist_not_checked = not self\
            ._validate_checklists(checklist_status_dtos,
                                  mandatory_checklist_dtos)

        if is_mandatory_checklist_not_checked:
            self.project_presenter.raise_checklist_not_satisfied_exception()

        satisfied_checkpoints_ids = self\
            ._get_checkpoint_ids_from_list_of_dtos(checklist_status_dtos)

        task_details_dto = self.task_storage.update_task_state(
            task_id,
            to_state_id,
            satisfied_checkpoints_ids
            )

        response = self.task_presenter.get_task_details_response(task_details_dto)

        return response

    @staticmethod
    def _convert_transition_data_to_dto(transition_data):
        transition_dto = TransitionDto(
            from_state_id=transition_data.get('from_state_id'),
            to_state_id=transition_data.get('to_state_id'),
            name=transition_data.get('name'),
            description=transition_data.get('description')
            )
        return transition_dto

    def _convert_update_task_state_input_data_to_dto(
            self,
            update_task_state_input_data,
            from_state_id):

        checklist = update_task_state_input_data['checklist']

        checklist_dtos = [
            self._convert_checklist_data_to_dto(checkpoint)
            for checkpoint in checklist
            ]

        update_task_state_query_dto = UpdateTransitionInputDto(
            project_id=update_task_state_input_data['project_id'],
            task_id=update_task_state_input_data['task_id'],
            from_state_id=from_state_id,
            to_state_id=update_task_state_input_data['to_state_id'],
            checklist=checklist_dtos)

        return update_task_state_query_dto

    @staticmethod
    def _convert_checklist_data_to_dto(checklist):

        checklist_dto = ChecklistStatusDto(
            checklist_id=checklist['checklist_id'],
            is_checked=checklist['is_checked'])

        return checklist_dto

    def _validate_checklists(self,
                             checklist_dtos,
                             mandatory_checklist_dtos):

        satisfied_checkpoints_dtos = [
            checkpoint_dto
            for checkpoint_dto in checklist_dtos
            if self._is_checked(checkpoint_dto)
            ]

        mandatory_checkpoint_ids = self._get_checkpoint_ids_from_list_of_dtos(
            mandatory_checklist_dtos)

        satisfied_checkpoint_ids = self._get_checkpoint_ids_from_list_of_dtos(
            satisfied_checkpoints_dtos)

        is_checklist_satisfied = \
            set(mandatory_checkpoint_ids).issubset(satisfied_checkpoint_ids)

        print("\n"*2,mandatory_checkpoint_ids)
        print("\n"*2,satisfied_checkpoint_ids)
        print("\n"*2,is_checklist_satisfied)

        return is_checklist_satisfied

    @staticmethod
    def _is_checked(checkpoint_dto):
        return checkpoint_dto.is_checked

    @staticmethod
    def _get_checkpoint_ids_from_list_of_dtos(checkpoints_dtos):

        list_of_ids = [
            checkpoint_dto.checklist_id
            for checkpoint_dto in checkpoints_dtos
            ]
        return list_of_ids
