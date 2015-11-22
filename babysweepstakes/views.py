import colander
from pyramid.httpexceptions import (
    HTTPFound,
    )
from pyramid.view import view_config, view_defaults

from .models import (
    DBSession,
    Guess,
    )


class GuessValidation(colander.MappingSchema):
    your_name = colander.SchemaNode(colander.String())
    baby_sex = colander.SchemaNode(colander.String(), validator=colander.OneOf(['Boy', 'Girl']))
    days_late = colander.SchemaNode(colander.Int())
    pounds = colander.SchemaNode(colander.Int())
    ounces = colander.SchemaNode(colander.Int())


@view_defaults(route_name='enter_guess')
class GuessViews:
    def __init__(self, request):
        self.request = request

    @view_config(renderer='templates/new.jinja2')
    def new_guess(self):
        params = self.request.params
        values = {
            'your_name': params.get('your_name', ''),
            'baby_sex': params.get('baby_sex', ''),
            'days_late': params.get('days_late', 0),
            'pounds': params.get('pounds', 7),
            'ounces': params.get('ounces', 6),
        }

        if 'submit' in params:
            schema = GuessValidation()
            try:
                guess = schema.deserialize(params)

                all_in_ounces = guess['pounds'] * 16 + guess['ounces']
                guess = Guess(your_name=guess['your_name'], baby_sex=guess['baby_sex'],
                              days_late=guess['days_late'], ounces=all_in_ounces)
                DBSession.add(guess)
                return HTTPFound(location=self.request.route_url('show_guesses'))
            except colander.Invalid as e:
                values.update({"error_" + key: value for key, value in e.asdict().items()})

        return values


    @view_config(route_name='show_guesses', renderer='templates/guesses.jinja2')
    def guesses(self):
        return {'guesses': DBSession.query(Guess).order_by(Guess.id).all()}
