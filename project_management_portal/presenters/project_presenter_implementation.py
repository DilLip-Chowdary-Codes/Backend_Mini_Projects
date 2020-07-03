from typing import List

from project_management_portal.interactors\
    .presenters.project_presenter_interface\
    import ProjectPresenterInterface

from django_swagger_utils.drf_server.exceptions\
    import NotFound, Unauthorized, BadRequest

from project_management_portal.constants.exception_messages\
    import INVALID_WORKFLOW,\
           INVALID_PROJECT,\
           UN_AUTHORIZED_DEVELOPER,\
           INVALID_TRANSITION,\
           CHECKLIST_NOT_SATISFIED,\
           INVALID_LIMIT,\
           INVALID_OFFSET

from project_management_portal.dtos\
    import UserDto, ProjectDto, ProjectsDetailsDto

class ProjectPresenterImplementation(ProjectPresenterInterface):

    def raise_invalid_workflow_id_exception(self):
        raise NotFound(*INVALID_WORKFLOW)

    def raise_invalid_project_id_exception(self):
        raise NotFound(*INVALID_PROJECT)

    def raise_invalid_transition_exception(self):
        raise NotFound(*INVALID_TRANSITION)

    def raise_unauthorized_developer_exception(self):
        raise Unauthorized(*UN_AUTHORIZED_DEVELOPER)

    def raise_invalid_limit_value_exception(self):
        raise BadRequest(*INVALID_LIMIT)

    def raise_invalid_offset_value_exception(self):
        raise BadRequest(*INVALID_OFFSET)

    def get_project_details_response(
            self,
            projects_details_dto: ProjectsDetailsDto
            ):

        project_details = self.get_projects_response(
            total_projects_count=1,
            projects_details_dto=projects_details_dto)['projects'][0]

        return project_details

    def get_projects_response(self,
                              total_projects_count: int,
                              projects_details_dto: ProjectsDetailsDto):

        user_project_dtos = projects_details_dto.project_dtos
        user_dtos = projects_details_dto.user_dtos

        projects_details_dict = [
            self._prepare_project_details_dict(project_dto, user_dtos)
            for project_dto in user_project_dtos
            ]

        response = {
            "total_projects": total_projects_count,
            "projects": projects_details_dict
        }
        return response

    def get_transition_details_response(self, transition_details_dtos):

        from_state_dto = transition_details_dtos.from_state
        to_state_dto = transition_details_dtos.to_state
        checklist_dtos = transition_details_dtos.checklist

        checklist_dicts = [
            self._convert_checklist_dto_to_dict(checklist_dto)
            for checklist_dto in checklist_dtos
            ]

        transition_details_response = {
            "from_state": self._convert_state_dto_to_dict(from_state_dto),
            "to_state": self._convert_state_dto_to_dict(to_state_dto),
            "check_list": checklist_dicts
        }

        return transition_details_response

    def raise_checklist_not_satisfied_exception(self):
        raise BadRequest(*CHECKLIST_NOT_SATISFIED)


    def _prepare_project_details_dict(self, project_dto: ProjectDto,
                                     user_dtos: List[UserDto]
                                    ):
        created_by_id = project_dto.created_by_id
        creator_details = self._prepare_user_details(
            user_dtos=user_dtos,
            user_id=created_by_id
            )
        developers_ids = project_dto.developers_ids

        developers_details = [
            self._prepare_user_details(user_dtos=user_dtos,
                                      user_id=developer_id
                                     )
            for developer_id in developers_ids
            ]

        project_details = {
            "project_id": project_dto.project_id,
            "name": project_dto.name,
            "description": project_dto.description,
            "workflow": project_dto.workflow,
            "project_type": project_dto.project_type,
            "created_by": creator_details,
            "created_at": str(project_dto.created_at),
            "developers": developers_details
        }
        return project_details

    def _prepare_user_details(self, user_dtos: List[UserDto], user_id: int):

        required_user_dto = None
        for user_dto in user_dtos:
            is_user_matched = user_id == user_dto.user_id

            if is_user_matched:
                required_user_dto = user_dto
                break

        user_details = self._convert_user_dto_to_dict(required_user_dto)
        return user_details

    @staticmethod
    def _convert_user_dto_to_dict(user_dto: UserDto):
        user_dict = {
            "user_id": user_dto.user_id,
            "username": user_dto.username,
            "profile_pic": user_dto.profile_pic,
            "phone_no": user_dto.phone_no
        }

        return user_dict

    @staticmethod
    def _convert_checklist_dto_to_dict(checklist_dto):

        checklist_dict = {
                  "checklist_id": checklist_dto.checklist_id,
                  "name": checklist_dto.name,
                  "is_required": checklist_dto.is_required
                }

        return checklist_dict

    @staticmethod
    def _convert_state_dto_to_dict(state_details_dto):
        state_details_dict = {
            "state_id":state_details_dto.state_id,
            "name":state_details_dto.name
        }
        return state_details_dict
