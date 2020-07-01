import pytest
from freezegun import freeze_time
from datetime import datetime
from project_management_portal.dtos import UserDto
from project_management_portal.models\
    import Developer, Workflow, Project, State, Task, Transition, Checklist
from oauth2_provider.models import AccessToken

# @pytest.fixture()
# def users():
#     password = "admin@123"
#     users_list = [
#         User(
#             username="username_1",
#             is_admin=True,
#             profile_pic="http://www.google.com",
#             phone_no="9999999999"
#             ),
#         User(
#             username="username_2",
#             is_admin=False,
#             profile_pic="http://www.google.com",
#             phone_no="9999999999"
#             ),
#         User(
#             username="username_3",
#             is_admin=True,
#             profile_pic="http://www.google.com",
#             phone_no="9999999999"
#             ),
#             ]
#     User.objects.bulk_create(users_list)
#     users_objects = list(User.objects.all())
#     for user in users_objects:
#         user.set_password(password)
#         user.save()

#     return users_objects
@pytest.fixture()
def user_dto():
    user_dto = UserDto(
        user_id=1,
        username="username_1",
        is_admin=False,
        profile_pic="http://www.google.com",
        phone_no="9999999999"
        )

    return user_dto

@pytest.fixture()
def user_admin_dto():
    user_admin_dto = UserDto(
        user_id=1,
        username="username_1",
        is_admin=True,
        profile_pic="http://www.google.com",
        phone_no="9999999999"
        )

    return user_admin_dto

@pytest.fixture
def states():
    states_list = [
        State(name="State_1"),
        State(name="State_2"),
        State(name="State_3"),
        ]
    State.objects.bulk_create(states_list)
    states = State.objects.all()
    return states

@pytest.fixture
def checklist():
    checklist_list = [
        Checklist(name="Check_1", is_required=True),
        Checklist(name="Check_2", is_required=False),
        Checklist(name="Check_3", is_required=True),
        Checklist(name="Check_4", is_required=False)
        ]

    Checklist.objects.bulk_create(checklist_list)
    checklist_objs = Checklist.objects.all()
    return checklist_objs

@pytest.fixture
def transitions(states, checklist):
    transitions_list = [
        Transition(
            name="transition_1",
            from_state_id=1,
            to_state_id=2,
            description="some content"),
        Transition(
            name="transition_2",
            from_state_id=2,
            to_state_id=3,
            description="some content"),
        Transition(
            name="transition_3",
            from_state_id=1,
            to_state_id=3,
            description="some content")
        ]
    Transition.objects.bulk_create(transitions_list)

    transitions = Transition.objects.all()

    [
        transition.checklist.set(checklist)
        for transition in transitions
    ]
    transitions[2].checklist.set([])

    return transitions

@pytest.fixture
def workflows(states, transitions):
    workflows_list = [
        Workflow(name="Workflow_1", created_by_id=1),
        Workflow(name="Workflow_2",  created_by_id=1)
        ]
    with freeze_time("2020-05-28 10:06:23"):
        Workflow.objects.bulk_create(workflows_list)
    workflows = Workflow.objects.all()
    workflows[0].states.set(states)
    workflows[0].transitions.set(transitions)
    return workflows

@pytest.fixture
def workflows_with_no_transition(states, transitions):

    workflows_list = [
        Workflow(name="Workflow_1", created_by_id=1),
        Workflow(name="Workflow_2", created_by_id=1)
        ]
    with freeze_time("2020-05-28 10:06:23"):
        Workflow.objects.bulk_create(workflows_list)
    workflows = Workflow.objects.all()
    workflows[0].states.set(states)
    return workflows

@pytest.fixture
def workflows_with_no_states(transitions):
    workflows_list = [
        Workflow(name="Workflow_1", created_by_id=1),
        Workflow(name="Workflow_2", created_by_id=1)
        ]
    with freeze_time("2020-05-28 10:06:23"):
        Workflow.objects.bulk_create(workflows_list)
    workflows = Workflow.objects.all()
    workflows[0].transitions.set(transitions)
    return workflows

@pytest.fixture
def workflows_with_no_transitions(states):
    workflows_list = [
        Workflow(name="Workflow_1", created_by_id=1),
        Workflow(name="Workflow_2", created_by_id=1)
        ]
    with freeze_time("2020-05-28 10:06:23"):
        Workflow.objects.bulk_create(workflows_list)
    workflows = Workflow.objects.all()
    workflows[0].states.set(states)
    return workflows

@pytest.fixture
def projects(workflows):
    creator_1_id = 1
    developer_1_id = 1
    developer_2_id = 2
    workflow = workflows[0]

    projects_list = [
        Project(
            name="projectManagement",
            description="it's a blaw blaw blaw blaw  blaw blaw ",
            workflow=workflow,
            project_type="Classic Software",
            created_by_id=creator_1_id
            ),
        Project(
            name="projectManagement_2",
            description="it's a blaw blaw blaw blaw  blaw blaw ",
            workflow=workflow,
            project_type="Classic Software",
            created_by_id=creator_1_id
            )
        ]

    with freeze_time("2020-05-28 10:06:23"):
        Project.objects.bulk_create(projects_list)
        projects_list = Project.objects.all()

        project_1_id = projects_list[0].id
        project_2_id = projects_list[1].id

        developers_list = [
            Developer(user_id=developer_1_id, project_id=project_1_id),
            Developer(user_id=developer_2_id, project_id=project_1_id),
            Developer(user_id=developer_2_id, project_id=project_2_id),
            ]
        Developer.objects.bulk_create(developers_list)

    return projects_list

@pytest.fixture
def projects_with_no_transitions_for_state(
    workflows_with_no_transition):

    workflows = workflows_with_no_transition
    creator_1_id = 1
    developer_1_id = 1
    developer_2_id = 2
    workflow = workflows[0]

    projects_list = [
        Project(
            name="projectManagement",
            description="it's a blaw blaw blaw blaw  blaw blaw ",
            workflow=workflow,
            project_type="Classic Software",
            created_by_id=creator_1_id
            ),
        Project(
            name="projectManagement_2",
            description="it's a blaw blaw blaw blaw  blaw blaw ",
            workflow=workflow,
            project_type="Classic Software",
            created_by_id=creator_1_id
            )
        ]
    with freeze_time("2020-05-28 10:06:23"):
        Project.objects.bulk_create(projects_list)
        projects_list = Project.objects.all()

        project_1_id = projects_list[0].id
        project_2_id = projects_list[1].id

        developers_list = [
            Developer(user_id=developer_1_id, project_id=project_1_id),
            Developer(user_id=developer_2_id, project_id=project_1_id),
            Developer(user_id=developer_2_id, project_id=project_2_id)
            ]

        Developer.objects.bulk_create(developers_list)

    return projects_list

@pytest.fixture
def tasks(projects, states):
    project = projects[0]
    state = states[0]
    state_2 = states[1]
    assignee_1_id = 1
    assignee_2_id = 2

    tasks_list = [
        Task(
            project=project,
            issue_type="Enhancement",
            title="Optimizing DB",
            assignee_id=assignee_1_id,
            description="string",
            state=state
            ),
        Task(
            project=project,
            issue_type="BUG",
            title="Optimizing DB",
            assignee_id=assignee_2_id,
            description="string",
            state=state_2
            )
        ]

    tasks = Task.objects.bulk_create(tasks_list)
    return tasks

@pytest.fixture
def tasks_with_projects_having_no_transition_state(
    projects_with_no_transitions_for_state, states):

    projects = projects_with_no_transitions_for_state
    project = projects[0]
    state = states[0]
    state_2 = states[1]
    assignee_1_id = 1
    assignee_2_id = 2

    tasks_list = [
        Task(
            project=project,
            issue_type="Enhancement",
            title="Optimizing DB",
            assignee_id=assignee_1_id,
            description="string",
            state=state
            ),
        Task(
            project=project,
            issue_type="BUG",
            title="Optimizing DB",
            assignee_id=assignee_2_id,
            description="string",
            state=state_2
            )
        ]

    tasks = Task.objects.bulk_create(tasks_list)
    return tasks

@pytest.fixture
def access_tokens():
    access_tokens_list = [
        AccessToken(
            user_id=1,
            token="test_access_token",
            expires=datetime.now()
            )
        ]

    with freeze_time("2020-05-28 10:06:23"):
        AccessToken.objects.bulk_create(access_tokens_list)
    access_tokens_objs = AccessToken.objects.all()
    return access_tokens_objs
