from project_management_portal.interactors.presenters\
    .task_presenter_interface import TaskPresenterInterface

from django_swagger_utils.drf_server.exceptions\
    import NotFound, Unauthorized

from project_management_portal.constants.exception_messages\
    import INVALID_STATE,\
        INVALID_WORKFLOW, INVALID_TASK, INVALID_TRANSITION

from project_management_portal.presenters.project_presenter_implementation\
        import ProjectPresenterImplementation

class TaskPresenterImplementation(TaskPresenterInterface):

    def raise_invalid_state_id_exception(self):
        raise NotFound(*INVALID_STATE)

    def raise_invalid_task_id_exception(self):
        raise NotFound(*INVALID_TASK)

    def get_create_task_response(self, task_details_dto):

        project_utils = ProjectPresenterImplementation()
        project_dto = task_details_dto.project
        project_details = project_utils.get_project_details_response(
            project_dto)
        assignee_id = task_details_dto.assignee_id

        task_details_response = {
            "project": project_details,
            "task_id": task_details_dto.task_id,
            "issue_type": task_details_dto.issue_type,
            "title": task_details_dto.title,
            "assignee_id": assignee_id,
            "description": task_details_dto.description,
            "state": task_details_dto.state
        }

        return task_details_response

    def get_tasks_response(self, tasks_details_dtos):

        project_utils = ProjectPresenterImplementation()
        is_tasks_not_empty = tasks_details_dtos
        if is_tasks_not_empty:

            project_dto = tasks_details_dtos[0].project

            project_details = project_utils.get_project_details_response(
                project_dto)
        else:
            project_details = {}

        tasks_details_responses = [
            self.get_create_task_response(task_details_dto)
            for task_details_dto in tasks_details_dtos
            ]

        tasks_details_response = []

        for task_details_response in tasks_details_responses:
            task_details_response.pop('project')
            tasks_details_response.append(task_details_response)

        response = {
            "total_tasks": len(tasks_details_dtos),
            "project" : project_details,
            "tasks": tasks_details_response
        }
        return response

    def get_task_details_response(self, task_details_dto):
        task_details_response = self.get_create_task_response(
            task_details_dto
            )
        return task_details_response

    def get_task_states_response(self, states_details_dtos):

        states_dicts = [
            self._convert_state_dto_to_dict(state_details_dto)
            for state_details_dto in states_details_dtos
            ]

        task_states_response = {
            "total_states": len(states_details_dtos),
            "states": states_dicts
        }

        return task_states_response

    @staticmethod
    def _convert_user_dto_to_dict(user_dto):
        user_details = {
            "user_id": user_dto.user_id,
            "username": user_dto.username,
            "profile_pic": user_dto.profile_pic,
            "phone_no": user_dto.phone_no
        }

        return user_details

    @staticmethod
    def _convert_state_dto_to_dict(state_details_dto):
        state_details_dict = {
            "state_id":state_details_dto.state_id,
            "name":state_details_dto.name
        }
        return state_details_dict
