import reflex as rx
from link_bio.routes import Route
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Color, Spacing


def index_links() -> rx.Component:
    return rx.vstack(
        title("Estadísticas"),
        link_button(
            "Vea datos interesantes en gráficas",
            "Análisis de datos en base a las peticiones que se realizan a Medichatter y datos globales",
            "/icons/sql.svg",
            Route.COURSES.value,
            False,
            Color.SECONDARY.value
        ),

        width="100%",
        spacing=Spacing.DEFAULT.value,
    )

""" 
        link_button(
            "Botón genérico",
            "texto aqui",
            "/icons/github.svg",
            const.GITHUB_URL
        ),
 """