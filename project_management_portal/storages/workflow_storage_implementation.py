from django.db.models import Prefetch
from project_management_portal.interactors\
    .storages.workflow_storage_interface import WorkflowStorageInterface

from project_management_portal.dtos\
    import StateDto, WorkflowDetailsDto,\
           TransitionDetailsDto, ChecklistDetailsDto

from project_management_portal.models import Workflow, Transition
class WorkflowStorageImplementation(WorkflowStorageInterface):

    def get_workflows(self):
        transition_set = Transition.objects\
            .select_related('from_state', 'to_state')\
            .prefetch_related('checklist')
            

        workflows = Workflow.objects.prefetch_related(
            Prefetch('states'),
            Prefetch('transitions', queryset=transition_set)
            ).all()
        # workflows = Workflow.objects.all()
        workflow_details_dtos = [
            self._convert_workflow_obj_to_workflow_details_dto(workflow)
            for workflow in workflows
            ]
        return workflow_details_dtos

    def _convert_workflow_obj_to_workflow_details_dto(
        self,
        workflow: object
        ):

        states = workflow.states.all()
        transitions = workflow.transitions.all()

        states_dtos = [
            self._convert_state_obj_to_state_dto(state)
            for state in states
            ]
        transitions_dtos = [
            self._convert_transition_obj_to_dto(transition)
            for transition in transitions
            ]

        workflow_details_dto = WorkflowDetailsDto(
            workflow_id=workflow.id,
            name=workflow.name,
            states=states_dtos,
            transitions=transitions_dtos,
            created_at=str(workflow.created_at)
            )

        return workflow_details_dto

    @staticmethod
    def _convert_state_obj_to_state_dto(state):
        state_dto = StateDto(name=state.name)
        return state_dto

    def _convert_transition_obj_to_dto(self, transition):
        
        checklist = transition.checklist.all()
        checklist_details_dtos = [
            self._convert_checklist_obj_to_checklist_details_dto(checkpoint)
            for checkpoint in checklist
            ]

        transition_dto = TransitionDetailsDto(
            name=transition.name,
            from_state=transition.from_state.name,
            to_state=transition.to_state.name,
            description=transition.description,
            checklist=checklist_details_dtos
            )
        return transition_dto
    
    @staticmethod
    def _convert_checklist_obj_to_checklist_details_dto(checklist):
        checklist_details_dto = ChecklistDetailsDto(
            checklist_id=checklist.id,
            name=checklist.name,
            is_required=checklist.is_required
            )
        return checklist_details_dto
