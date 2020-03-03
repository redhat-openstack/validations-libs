#   Copyright 2020 Red Hat, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

import mock


VALIDATIONS_LIST = [{
    'description': 'My Validation One Description',
    'groups': ['prep', 'pre-deployment'],
    'id': 'my_val1',
    'name': 'My Validition One Name',
    'parameters': {}
}, {
    'description': 'My Validation Two Description',
    'groups': ['prep', 'pre-introspection'],
    'id': 'my_val2',
    'name': 'My Validition Two Name',
    'parameters': {'min_value': 8}
}]

GROUPS_LIST = [
    ('group1', 'Group1 description'),
    ('group2', 'Group2 description'),
    ('group3', 'Group3 description'),
]

VALIDATIONS_LOGS_CONTENTS_LIST = [{
    'plays': [{
        'play': {
            'duration': {
                'end': '2019-11-25T13:40:17.538611Z',
                'start': '2019-11-25T13:40:14.404623Z',
                'time_elapsed': '0:00:03.753'
            },
            'host': 'undercloud',
            'id': '008886df-d297-1eaa-2a74-000000000008',
            'validation_id': '512e',
            'validation_path':
            '/usr/share/openstack-tripleo-validations/playbooks'
        },
        'tasks': [
            {
                'hosts': {
                    'undercloud': {
                        '_ansible_no_log': False,
                        'action': 'command',
                        'changed': False,
                        'cmd': [u'ls', '/sys/class/block/'],
                        'delta': '0:00:00.018913',
                        'end': '2019-11-25 13:40:17.120368',
                        'invocation': {
                            'module_args': {
                                '_raw_params': 'ls /sys/class/block/',
                                '_uses_shell': False,
                                'argv': None,
                                'chdir': None,
                                'creates': None,
                                'executable': None,
                                'removes': None,
                                'stdin': None,
                                'stdin_add_newline': True,
                                'strip_empty_ends': True,
                                'warn': True
                            }
                        },
                        'rc': 0,
                        'start': '2019-11-25 13:40:17.101455',
                        'stderr': '',
                        'stderr_lines': [],
                        'stdout': 'vda',
                        'stdout_lines': [u'vda']
                    }
                },
                'task': {
                    'duration': {
                        'end': '2019-11-25T13:40:17.336687Z',
                        'start': '2019-11-25T13:40:14.529880Z'
                    },
                    'id':
                    '008886df-d297-1eaa-2a74-00000000000d',
                    'name':
                    'advanced-format-512e-support : List the available drives'
                }
            },
            {
                'hosts': {
                    'undercloud': {
                        'action':
                        'advanced_format',
                        'changed': False,
                        'msg':
                        'All items completed',
                        'results': [{
                            '_ansible_item_label': 'vda',
                            '_ansible_no_log': False,
                            'ansible_loop_var': 'item',
                            'changed': False,
                            'item': 'vda',
                            'skip_reason': 'Conditional result was False',
                            'skipped': True
                        }],
                        'skipped': True
                    }
                },
                'task': {
                    'duration': {
                        'end': '2019-11-25T13:40:17.538611Z',
                        'start': '2019-11-25T13:40:17.341704Z'
                    },
                    'id': '008886df-d297-1eaa-2a74-00000000000e',
                    'name':
                    'advanced-format-512e-support: Detect the drive'
                }
            }
        ]
    }],
    'stats': {
        'undercloud': {
            'changed': 0,
            'failures': 0,
            'ignored': 0,
            'ok': 1,
            'rescued': 0,
            'skipped': 1,
            'unreachable': 0
        }
    },
    'validation_output': []
}]
