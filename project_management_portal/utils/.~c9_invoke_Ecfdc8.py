from freezegun import freeze_time
from django_swagger_utils.utils.test import CustomAPITestCase
from project_management_portal import models
from project_management_portal.utils.factories\
    import\
        DeveloperFactory,\
        StateFactory,\
        ChecklistFactory, TransitionFactory,\
        WorkflowFactory, ProjectFactory,\
        TaskFactory

class CustomTestUtils(CustomAPITestCase):

    def reset(self):
        StateFactory.reset_sequence(1)
        ChecklistFactory.reset_sequence(1)
        TransitionFactory.reset_sequence(1)
        WorkflowFactory.reset_sequence(1)
        ProjectFactory.reset_sequence(1)
        TaskFactory.reset_sequence(1)
        DeveloperFactory.reset_sequence()
        # ProjectFactory.created_by_id.reset()
        ProjectFactory.project_type.reset()
        # WorkflowFactory.created_by_id.reset()
        TaskFactory.issue_type.reset()

    def remove_token(self):
        from oauth2_provider.models import AccessToken
        # AccessToken.objects.filter(user_id=1).delete()
        print(AccessToken.objects.all())

    @freeze_time("2020-06-26")
    def create_workflow(self):
        from project_management_portal.models import Transition
        self.reset()
        states = StateFactory.create_batch(size=4)
        checklist = ChecklistFactory.create_batch(size=5)
        TransitionFactory(from_state_id=1, to_state_id=2, checklist=checklist)
        TransitionFactory(from_state_id=2, to_state_id=3, checklist=checklist)
        TransitionFactory(from_state_id=3, to_state_id=4, checklist=checklist)
        TransitionFactory(from_state_id=2, to_state_id=1, checklist=checklist)
        TransitionFactory(from_state_id=3, to_state_id=1, checklist=checklist)

        transitions = Transition.objects.all()
        workflow = WorkflowFactory.create(
            states=states,
            transitions=transitions)

        return workflow

    @freeze_time("2020-06-26")
    def create_project(self):
        self.reset()
        ProjectFactory.project_type.reset()

        workflow = self.create_workflow()
        DeveloperFactory.create_batch(size=2, project_id=1)
        ProjectFactory(workflow=workflow)
        TaskFactory.create_batch(size=5,
                                 project_id=1,
                                 assignee_id=1,
                                 state_id=1)

    def create_task(self):
        self.reset()
        checklist = ChecklistFactory.create_batch(size=5)
        TaskFactory(state_id=1,
                    conditions_satisfied = checklist
                   )

    def create_workflows(self):
        self.reset()
        WorkflowFactory.create_batch(size=5, created_by_id=1)

    @freeze_time("2020-06-26")
    def create_projects(self, user_id=None):
        self.reset()

        if not user_id:
            user_id = 1

        workflow = self.create_workflow()
        ProjectFactory.create_batch(size=6,
                                    workflow=workflow,
                                    created_by_id=user_id)
        DeveloperFactory.create_batch(size=2, project_id=1)
        DeveloperFactory.create_batch(size=2, project_id=2)
        DeveloperFactory.create_batch(size=2, project_id=3)

    @freeze_time("2020-06-26")
    def create_projects_for_admin(self):
        self.reset()
        workflow = self.create_workflow()
        ProjectFactory.create_batch(size=3,
                                    workflow=workflow,
                                    created_by_id=1)
