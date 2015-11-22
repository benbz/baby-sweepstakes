from pyramid.httpexceptions import (
    HTTPFound,
    )
from pyramid.view import view_config

from .models import (
    DBSession,
    Guess,
    )


@view_config(route_name='home', renderer='templates/new.jinja2')
def my_view(request):
    return {'project': 'BabySweepstakes'}


@view_config(route_name='new_guess')
def new_guess(request):
    your_name = request.params['your_name']
    baby_sex = request.params['baby_sex']
    days_late = request.params['days_late']
    guess = Guess(your_name=your_name, baby_sex=baby_sex, days_late=days_late)
    DBSession.add(guess)
    return HTTPFound(location=request.route_url('guesses'))


@view_config(route_name='guesses', renderer='templates/guesses.jinja2')
def guesses(request):
    return {'guesses': DBSession.query(Guess).order_by(Guess.id).all()}
