from settings.environment.base import *

DATABASES = {
    'default':
        read_pgpass('dbpcnqi601eh1t')
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-prod.json'),
    }
}
