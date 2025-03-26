# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Monthcalendar(Component):
    """A Monthcalendar component.


Keyword arguments:

- id (string; optional)

- className (string; optional)

- selectedDate (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'monthcalendar'
    _type = 'Monthcalendar'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        selectedDate: typing.Optional[str] = None,
        className: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'className', 'selectedDate']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'selectedDate']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Monthcalendar, self).__init__(**args)
