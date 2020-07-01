# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestWorkFlowPresenter.test_get_workflows_response workflow_details'] = {
    'total_workflows': 2,
    'workflows': [
        {
            'name': 'workflow_1',
            'workflow_id': 1
        },
        {
            'name': 'workflow_2',
            'workflow_id': 2
        }
    ]
}

snapshots['TestWorkFlowPresenter.test_get_workflows_response_with_no_workflows workflow_details'] = {
    'total_workflows': 0,
    'workflows': [
    ]
}
