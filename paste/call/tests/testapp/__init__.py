gconf = {}

def app_factory(global_config, **local_config):
    global gconf
    gconf = global_config
    gconf['status'] = 'initialized'
    gconf['db'] = local_config.get('db')
    return None

def exec_in_environ(*args, **kargs):
    print 'Working in app status %s' % gconf['status']
    print 'Using db: %s' % gconf['db']
