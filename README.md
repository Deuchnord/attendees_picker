# Attendees Picker

A small library to help to pick attendees for your events.

## Usage

The library provides a function named `pick_attendees()` which takes three parameters:

- `max_attendeed`: the maximum number of attendees that the event can accept
- `organizers`: a list of people who organize the event
- `candidates`: a list of people who have shown an interest to the event

The function returns a list that contains:

- all the organizers
- random people among the candidates

For instance, if you write:

```python
from attendees_picker import pick_attendees

attendees = pick_attendees(5, organizers=["Alice", "Bob"], candidates=["Charles", "David", "Eliot", "Frederic"])
```

Then the returned `attendees` variable might return:

```python
['Alice', 'Bob', 'Frederic', 'David', 'Charles']
```

Note that the candidates may not be in the same order as the one in the initial function call.
