# Enable HTTP methods
RESOURCE_METHODS = ['GET', 'POST']

DOMAIN = {

	'user': {
		'additional_lookup': {
        	'url': 'regex("[\w]+")',
        	'field': 'username',
        },
		'schema': {
            'first_name': {
                'type': 'string'
            },
            'last_name': {
                'type': 'string'
            },
            'email': {
                'type': 'string',
                'unique': True
            },
            'username': {
                'type': 'string',
                'unique': True
            },
            'password': {
                'type': 'string'
            },
            'activated': {
                'type': 'boolean',
                'default': True
            }
        }
	},

	'cookbook': {
		'schema': {
			'name': {
                'type': 'string'
            },
            'description': {
                'type': 'text',
                'default': ''
            },
            'author': {
                'type': 'integer'
            },
            'photo': {
                'type': 'string'
                'default': ''
            }
		}
	}
}