import reflex as rx
import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size, Color, Spacing
from link_bio.routes import Route
from link_bio.state import DataState

def courses_links() -> rx.Component:
    return rx.vstack(
        title("Estadísticas"),
        link_button(
            "Regresar",
            "¡Continúa hablando con MediChatter!",
            "/icons/return.png",
            Route.INDEX.value,
            False,
            Color.SECONDARY.value
        ),

        rx.link(
            rx.hstack(
                rx.text(
                    "Expectativa de vida al nacer a nivel global",
                    font_size=Size.DEFAULT.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href="https://ourworldindata.org/grapher/life-expectancy",
            is_external=True
        ),

        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="edad",
            ),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            data=DataState.data_life,
            width="100%",
            height=200,
        ),

        rx.link(
            rx.hstack(
                rx.text(
                    "Muertes por diabetes a nivel mundial en los últimos 50 años.",
                    font_size=Size.DEFAULT.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href="https://ourworldindata.org/grapher/deaths-from-diabetes-by-type",
            is_external=True
        ),

        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="muertes",
            ),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            data=DataState.data_diabetes,
            width="100%",
            height=200,
        ),

        rx.link(
            rx.hstack(
                rx.text(
                    "Muertes por COVID-19 estimadas de forma acumulativa a nivel mundial (en millones).",
                    font_size=Size.DEFAULT.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href="https://ourworldindata.org/grapher/excess-deaths-cumulative-economist-single-entity",
            is_external=True
        ),

        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="muertes",
            ),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            data=DataState.data_covid,
            width="100%",
            height=200,
        ),

        rx.link(
            rx.hstack(
                rx.text(
                    "Muertes por cancer (en cientos de miles)",
                    font_size=Size.DEFAULT.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href="https://ourworldindata.org/grapher/cancer-death-rates?tab=chart",
            is_external=True
        ),

        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="muertes",
            ),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            data=DataState.data_cancer,
            width="100%",
            height=200,
        ),

        width="100%",
        spacing=Spacing.DEFAULT.value,
        on_mount=DataState.load_all_data,
    )