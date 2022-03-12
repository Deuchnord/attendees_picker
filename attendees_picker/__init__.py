#!/usr/bin/env python3

import random
from warnings import warn


class ValueWarning(RuntimeWarning):
    pass


class MaxAttendeeWarning(ValueWarning):
    def __init__(self, required_max: int, actual_max: int):
        super().__init__(
            f"A maximum of {required_max} attendees has been required, but only {actual_max} people provided. "
            "Everyone will be able to participate."
        )


class TooManyOrganizersError(ValueError):
    def __init__(self, required_max: int, number_organizers: int):
        super().__init__(
            f"A maximum number of {required_max} attendees has been required, but {number_organizers} organizers given. "
            "No candidates will be able to join."
        )


def pick_attendees(max_attendees: int, organizers: [str], candidates: [str]) -> [str]:
    """Pick attendees from the given candidates

    Only the given max number of attendees are selected. The organizers are always selected and are at the beginning
    of the returned list.

    >>> attendees = pick_attendees(5, organizers=["Alice", "Bob"], candidates=["Charles", "David", "Eliot", "Frederic"])
    >>> len(attendees)
    5
    >>> attendees[0:2]
    ['Alice', 'Bob']

    If there is enough place for everyone, a warning will be emitted, and a list of all people will be returned.

    >>> import sys; sys.stderr = sys.stdout
    >>> import doctest; doctest.ELLIPSIS_MARKER = '[...]'
    >>> pick_attendees(5, organizers=["Alice", "Bob"], candidates=["Charles", "David", "Eliot"]) # doctest: +ELLIPSIS
    [...] MaxAttendeeWarning: A maximum of 5 attendees has been required, but only 5 people provided. Everyone will be able to participate.
        warn(MaxAttendeeWarning(max_attendees, people_number))
    ['Alice', 'Bob', 'Charles', 'David', 'Eliot']

    An error is raised if too many organizers are given in comparison to the number of maximum attendees.

    >>> pick_attendees(2, organizers=["Alice", "Bob"], candidates=["Charles", "David", "Eliot"])
    Traceback (most recent call last):
        ...
    attendees_picker.TooManyOrganizersError: A maximum number of 2 attendees has been required, but 2 organizers given. No candidates will be able to join.
    """
    people_number = len(candidates + organizers)

    if people_number <= max_attendees:
        warn(MaxAttendeeWarning(max_attendees, people_number))
        return organizers + candidates

    if max_attendees <= len(organizers):
        raise TooManyOrganizersError(max_attendees, len(organizers))

    random.shuffle(candidates)
    return organizers + candidates[: max_attendees - len(organizers)]
