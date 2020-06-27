import factory
from project_management_portal import models
from project_management_portal.constants.enums import Project_Type
from project_management_portal.constants.enums import IssueType

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.User

    username = factory.Sequence(lambda n: f'user_{n}')

class StateFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.State
    name = factory.Sequence(lambda n: f'state_{n}')

class ChecklistFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Checklist

    name = factory.Sequence(lambda n: f'check_{n}')

class TransitionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Transition

    name = factory.Sequence(lambda n: f'transition_{n}')
    from_state = factory.Iterator(models.State.objects.all())
    to_state = factory.Iterator(models.State.objects.all())

    @factory.post_generation
    def checklist(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for checkpoint in extracted:
                self.checklist.add(checkpoint)

    description = factory.LazyAttribute(
        lambda obj: f'{obj.from_state.name}-->{obj.to_state.name}'
    )

class WorkflowFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Workflow

    name = factory.Sequence(lambda n: 'workflow_%s' %n)

    @factory.post_generation
    def states(self, create, extracted, **kwargs):

        if not create:
            return

        if extracted:
            for state in extracted:
                self.states.add(state)

    @factory.post_generation
    def transitions(self, create, extracted, **kwargs):

        if not create:
            return

        if extracted:
            for transition in extracted:
                self.transitions.add(transition)

    created_by = factory.Iterator(models.User.objects.all())

class ProjectFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = models.Project
        
    name = factory.Sequence(lambda n: f'project_{n}')
    description = factory.Sequence(lambda n: f'project_{n}_description')
    workflow = factory.Iterator(models.Workflow.objects.all())
    project_type = factory.Iterator(
        [project_type.value for project_type in Project_Type])
    created_by = factory.Iterator(models.User.objects.all())
    
    @factory.post_generation
    def developers(self, create, extracted, **kwargs):

        if not create:
            return

        if extracted:
            for developer in extracted:
                self.developers.add(developer)

class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Task
    
    project = factory.Iterator(models.Project.objects.all())
    issue_type = factory.Iterator(
        issue_type.value for issue_type in IssueType
    )
    title = factory.Sequence(lambda n: f'task_{n}')
    assignee = factory.Iterator(models.User.objects.all())
    description = factory.Sequence(lambda n: f'description_{n}')
    state = factory.Iterator(models.State.objects.all())

    @factory.post_generation
    def conditions_satisfied(self, create, extracted, **kwargs):
        
        if not create:
            return
        
        if extracted:
            for checkpoint in extracted:
                self.conditions_satisfied.add(checkpoint)
