from pyramid.httpexceptions import (
    HTTPFound,
    )
from pyramid.view import view_config, view_defaults

from .models import (
    DBSession,
    Guess,
    )

@view_defaults(route_name='enter_guess')
class GuessViews:
    def __init__(self, request):
        self.request = request

    @view_config(renderer='templates/new.jinja2')
    def new_guess(self):
        return {}

    @view_config(request_method='POST')
    def save_guess(self):
        your_name = self.request.params['your_name']
        baby_sex = self.request.params['baby_sex']
        days_late = self.request.params['days_late']
        pounds = int(self.request.params['pounds'])
        just_ounces = int(self.request.params['ounces'])
        all_in_ounces = pounds * 16 + just_ounces
        guess = Guess(your_name=your_name, baby_sex=baby_sex, days_late=days_late, ounces=all_in_ounces)
        DBSession.add(guess)
        return HTTPFound(location=self.request.route_url('show_guesses'))

    @view_config(route_name='show_guesses', renderer='templates/guesses.jinja2')
    def guesses(self):
        return {'guesses': DBSession.query(Guess).order_by(Guess.id).all()}
