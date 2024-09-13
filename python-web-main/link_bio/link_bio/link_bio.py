import reflex as rx
import link_bio.constants as const
import link_bio.styles.styles as styles
from link_bio.pages.index import index
from link_bio.pages.graficas import courses

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

