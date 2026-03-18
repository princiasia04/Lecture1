import flet as ft

from gestionale.vendite.controller import Controller
from gestionale.vendite.view import View


def main (page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.set_controller(c)
    v.carica_interfaccia()

ft.app(target = main)