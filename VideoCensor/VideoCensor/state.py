"""Base state for the app."""

import reflex as rx


class State(rx.State):
    text: str = "Hello World!"

    pass
