from .elements import create_air, create_earth
import elements


def healing_potion() -> None:
    return f"Healing potion brewed with {create_earth()} and {create_air()}"


def strength_potion() -> None:
    return f"Strength potion brewed with {elements.create_fire()} and {elements.create_water()}"


def invisibility_potion() -> None:
    data = "Invisibility potion brewed with"
    return f"{data} {create_air()} and {elements.create_water()}"


def wisdom_potion() -> None:
    data = "Wisdom poriton brewed with all elements:"
    return f"{data} {create_air} {create_earth} {elements.create_fire()} {elements.create_water()}"
