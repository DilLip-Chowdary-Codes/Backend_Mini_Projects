from typing import  Optional, List
from django.db.models import Prefetch

from oauth2_provider.models import AccessToken, RefreshToken
from common.dtos import UserAuthTokensDTO
from project_management_portal.models\
    import User, Project, Workflow, Transition
from project_management_portal.dtos\
    import ProjectDto, UserDto, ProjectDetailsDto, TransitionDto,\
           TransitionDetailsDto, StateDetailsDto, ChecklistDetailsDto

from project_management_portal.interactors.storages.project_storage_interface\
    import ProjectStorageInterface

class ProjectStorageImplementation(ProjectStorageInterface):

    def validate_workflow_id(self, workflow_id: int) -> bool:
        is_workflow_valid = Workflow.objects.filter(id=workflow_id).exists()
        return is_workflow_valid

    def validate_admin_scope(self, user_id: int):
        is_admin = User.objects.get(user_id=user_id).is_admin
        return is_admin

    def validate_project_id(self, project_id: int):
        project = Project.objects.filter(id=project_id).first()
        project_exists = project
        if project_exists:
            project_dto = self._convert_project_object_to_dto(project)
        else:
            project_dto = None
        print("-",project_dto)
        return project_dto

    def validate_developer_for_project(
        self,
        user_id: int,
        project_id: int) -> bool:

        is_developer = Project.objects.filter(
            id=project_id,
            developers__user_id=user_id).exists()
        is_admin = Project.objects.filter(
            id=project_id,
            created_by_id=user_id).exists()

        is_user_authorized = is_developer or is_admin
        return is_user_authorized

    def validate_transition(self, workflow_id, from_state_id, to_state_id):
        is_transition_valid = Transition.objects\
                .filter(workflow__id=workflow_id,
                        from_state_id=from_state_id,
                        to_state_id=to_state_id).exists()
        return is_transition_valid

    def create_project(self,
                       user_id: int,
                       project_dto: ProjectDto
                      ) -> ProjectDetailsDto:

        project_obj = Project.objects.create(
            name=project_dto.name,
            description=project_dto.description,
            workflow_id=project_dto.workflow_id,
            project_type=project_dto.project_type,
            created_by_id=user_id
            )
        developers_user_ids = project_dto.developers
        developers_objs = User.objects.filter(user_id__in=developers_user_ids)

        project_obj.developers.set(developers_objs)
        project_details_dto = self\
            ._convert_project_object_to_project_details_dto(project_obj)

        return project_details_dto

    def get_projects_for_user(self,
                                      user_id: int,
                                      offset: int,
                                      limit: int) -> List[ProjectDto]:
        
        transition_set = Transition.objects\
            .select_related('from_state', 'to_state')

        workflow = Workflow.objects.prefetch_related(
            Prefetch('states'),
            Prefetch('transitions', queryset=transition_set)
            )

        user_projects = Project.objects\
            .select_related('created_by')\
            .prefetch_related(
                Prefetch('workflow', queryset=workflow),
                Prefetch('developers'))\
            .filter(developers__user_id=user_id)\
            .order_by('-created_at')[offset: offset + limit]


        project_dtos = [
            self._convert_project_object_to_project_details_dto(project)
            for project in user_projects
            ]

        return project_dtos

    def get_projects_for_admin(self,
                                     user_id: int,
                                     offset: int,
                                     limit: int) -> List[ProjectDto]:
        
        transition_set = Transition.objects\
            .select_related('from_state', 'to_state')

        workflow = Workflow.objects.prefetch_related(
            Prefetch('states'),
            Prefetch('transitions', queryset=transition_set)
            )

        admin_projects = Project.objects\
            .select_related('created_by')\
            .prefetch_related(
                Prefetch('workflow', queryset=workflow),
                Prefetch('developers'))\
            .filter(created_by_id=user_id)\
            .order_by('-created_at')[offset: offset + limit]

        project_dtos = [
            self._convert_project_object_to_project_details_dto(project)
            for project in admin_projects
            ]

        return project_dtos

    def get_user_projects_count(self, user_id):

        projects_count = Project.objects.filter(
            developers__user_id=user_id).count()
        return projects_count

    def get_admin_projects_count(self, user_id):

        projects_count = Project.objects.filter(
            created_by_id=user_id).count()
        return projects_count

    def get_workflow_id_of_project(self, project_id: int) -> int:

        workflow_id = Project.objects.get(id=project_id).workflow_id

        return workflow_id

    def validate_state_transition(self, workflow_id: int,
                            from_state_id: int, to_state_id: int):

        is_transition_valid = Transition.objects.filter(
            workflow__id=workflow_id,
            from_state_id=from_state_id,
            to_state_id=to_state_id).exists()

        return is_transition_valid

    def get_states_transition_details(self, get_transition_details_query_dto):

        project_id = get_transition_details_query_dto.project_id

        from_state_id = get_transition_details_query_dto.from_state_id
        to_state_id = get_transition_details_query_dto.to_state_id
        
        transition = Transition.objects\
            .select_related('from_state', 'to_state')\
            .prefetch_related('checklist')\
            .get(workflow__project__id=project_id,
                                            from_state_id=from_state_id,
                                            to_state_id=to_state_id)
        transition_details_dto = self\
            ._convert_transition_object_to_transition_details_dto(transition)
        return transition_details_dto

    def get_transition_mandatory_checklist(
            self, update_task_state_query_dto):

        project_id = update_task_state_query_dto.project_id
        from_state_id = update_task_state_query_dto.from_state_id
        to_state_id = update_task_state_query_dto.to_state_id

        transition = Transition.objects\
            .filter(workflow__project__id=project_id,
                    from_state_id=from_state_id,
                    to_state_id=to_state_id).first()

        transition_checklist = transition.checklist.filter(is_required=True)
        transition_checklist_dtos = [
            self._convert_checklist_obj_to_checklist_details_dto(checkpoint)
            for checkpoint in transition_checklist
            ]

        return transition_checklist_dtos

    def _convert_project_object_to_project_details_dto(self,
                                       project: object
                                      ) -> ProjectDetailsDto:
        creator_details = self._convert_user_object_to_dto(project.created_by)
        project_developers = project.developers.all()

        project_developers_dtos = [
            self._convert_user_object_to_dto(developer)
            for developer in project_developers
            ]

        project_details_dto = ProjectDetailsDto(
            project_id=project.id,
            name=project.name,
            description=project.description,
            workflow=project.workflow.name,
            project_type=project.project_type,
            created_by=creator_details,
            created_at=str(project.created_at),
            developers=project_developers_dtos
            )

        return project_details_dto

    @staticmethod
    def _convert_user_object_to_dto(user):
        user_dto = UserDto(
            user_id=user.user_id,
            username=user.username,
            profile_pic=user.profile_pic,
            phone_no=user.phone_no,
            is_admin=user.is_admin
            )
        return user_dto

    @staticmethod
    def _convert_transition_object_to_dto(transition):
        transition_dto = TransitionDto(
            name=transition.name,
            from_state_id=transition.from_state_id,
            to_state_id=transition.to_state_id,
            description=transition.description
            )

        return transition_dto

    @staticmethod
    def _convert_project_object_to_dto(project):
        project_dto = ProjectDto(
            name=project.name,
            description=project.description,
            workflow_id=project.workflow_id,
            project_type=project.project_type
            )

        return project_dto

    @staticmethod
    def _convert_state_obj_to_state_details_dto(state):

        state_details_dto = StateDetailsDto(
            state_id=state.id,
            name=state.name
            )

        return state_details_dto

    def _convert_transition_object_to_transition_details_dto(
            self, transition):

        checklist = transition.checklist.all()
        checklist_details_dtos = [
            self._convert_checklist_obj_to_checklist_details_dto(checkpoint)
            for checkpoint in checklist
            ]
        transition_details = TransitionDetailsDto(
            name=transition.name,
            from_state=self._convert_state_obj_to_state_details_dto(
                transition.from_state),
            to_state=self._convert_state_obj_to_state_details_dto(
                transition.to_state),
            checklist=checklist_details_dtos,
            description=transition.description
            )
        return transition_details

    @staticmethod
    def _convert_checklist_obj_to_checklist_details_dto(checklist):

        checklist_details_dto = ChecklistDetailsDto(
            name=checklist.name,
            is_required=checklist.is_required,
            checklist_id=checklist.id
            )

        return checklist_details_dto
