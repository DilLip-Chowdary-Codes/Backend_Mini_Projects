__author__ = 'ibhubs'

import json
from project_management_portal.models\
    import User, State, Transition, Workflow, Project, Checklist, Task

with open('project_management_portal/utils/data.json') as file:
    DATA = json.load(file)

class Fixture(object):
    """
    Class contains populate method as static method
    Is used by django-swagger-utils as a management command
    """

    @staticmethod
    def populate():

        """
        Populates data for app project_management_portal
        :return:
        """
        project_data = DATA['project_data']

        users = project_data['users']
        states = project_data['states']
        transitions = project_data['transitions']
        checklist = project_data['checklist']
        workflows = project_data['workflows']
        projects = project_data['projects']
        tasks = project_data['tasks']

        # users_list = [
        #     User(
        #         username=user['username'],
        #         profile_pic=user['profile_pic'],
        #         is_admin=user['is_admin'])
        #         for user in users
        #         ]
        # User.objects.bulk_create(users_list)
        # users = list(User.objects.all())
        # for user in users:
        #     user.set_password("admin@123")
        #     user.save()

        # states_list = [
        #     State(
        #         name=state['name'])
        #     for state in states]

        # State.objects.bulk_create(states_list)

        # checklist_list = [
        #     Checklist(
        #         name=checkpoint['name'],
        #         is_required=checkpoint['is_required']
        #         )
        #     for checkpoint in checklist]

        # Checklist.objects.bulk_create(checklist_list)

        # for transition in transitions:
        #     transition_obj = Transition.objects.create(
        #         name=transition['name'],
        #         from_state_id=transition['from_state_id'],
        #         to_state_id=transition['to_state_id'],
        #         description=transition['description']
        #         )

        #     checklist_objs = Checklist.objects.filter(
        #         id__in=transition['checklist'])
        #     transition_obj.checklist.set(checklist_objs)

        # for workflow in workflows:
        #     workflow_obj = Workflow.objects.create(
        #         name=workflow['name']
        #         )

        #     state_objs = State.objects.filter(
        #         id__in=workflow['states'])
        #     workflow_obj.states.set(state_objs)

        #     transition_objs = Transition.objects.filter(
        #         id__in=workflow['transitions'])
        #     workflow_obj.transitions.set(transition_objs)

        for project in projects:

            project_obj = Project.objects.create(
                name=project['name'],
                description=project['description'],
                workflow_id=project['workflow_id'],
                project_type=project['project_type'],
                created_by_id=project['created_by_id']
                )

            developer_objs = User.objects.filter(
                user_id__in=project['developers'])
            project_obj.developers.set(developer_objs)

        # for task in tasks:
        #     task_obj = Task.objects.create(
        #         project_id=task['project_id'],
        #         issue_type=task['issue_type'],
        #         title=task['title'],
        #         assignee_id=task['assignee_id'],
        #         description=task['description'],
        #         state_id=task['state_id']
        #         )

        #     checklist_objs = Checklist.objects.filter(
        #         id__in=task['conditons_satisfied'])

        #     task_obj.conditions_satisfied.set(checklist_objs)
