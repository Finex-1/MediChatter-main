import reflex as rx
import link_bio.constants as const
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.colors import Color, TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.png",
            height=Size.VERY_BIG.value,
            alt="Logotipo de la UNIS"
        ),
        rx.link(
            rx.box(
                f"© 2024 ",
                rx.text(
                    "Maximiliano González, Kevin González, Walter Orellana",
                    as_="span",
                    color=Color.PRIMARY.value
                ),
                padding_top=Size.DEFAULT.value
            ),
        ),
        rx.link(
            rx.hstack(
                rx.text(
                    "Proyecto de la Universidad del Istmo de Guatemala",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href=const.UNI_URL,
            is_external=True
        ),
        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value
    )
