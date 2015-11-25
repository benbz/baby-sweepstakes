import os
from pyramid.config import Configurator
from sqlalchemy import (
    create_engine,
    event,
    exc,
    )

from sqlalchemy.pool import Pool

from .models import (
    DBSession,
    Base,
    )


@event.listens_for(Pool, "checkout")
def ping_connection(dbapi_connection, connection_record, connection_proxy):
    cursor = dbapi_connection.cursor()
    try:
        cursor.execute("SELECT 1")
    except:
        raise exc.DisconnectionError()
    cursor.close()


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    sqlalchemy_url = os.path.expandvars(settings.get('sqlalchemy.url'))
    engine = create_engine(sqlalchemy_url, pool_recycle=3600)
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('enter_guess', '/')
    config.add_route('show_guesses', '/guesses')
    config.scan()
    return config.make_wsgi_app()
