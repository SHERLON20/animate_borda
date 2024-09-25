import flet as ft
import math
from asyncio import sleep
def main(page:ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    animate_border=ft.Ref[ft.Container]()
    snake_border=ft.Container(
        width=500,
        height=100,
        bgcolor=ft.colors.BLACK,
        border_radius=ft.border_radius.all(20),
        content=ft.Stack(
            aspect_ratio=16/9,
            controls=[
                ft.Container(
                    ref=animate_border,
                    gradient=ft.LinearGradient(
                        colors=[ft.colors.CYAN,ft.colors.RED]
                    ),
                    margin=ft.margin.symmetric(vertical=30),
                    rotate=ft.Rotate(angle=1),
                    scale=ft.Scale(scale_x=1.2),
                    animate_rotation=ft.Animation(duration=3000,curve=ft.AnimationCurve.LINEAR)

                ),
                ft.Container(
                    bgcolor=ft.colors.BLACK,
                    padding=ft.padding.all(20),
                    margin=ft.margin.all(8),
                    border_radius=ft.border_radius.all(15),
                    content=ft.Image(src='https://images3.alphacoders.com/133/1332803.png',exclude_from_semantics=True),
                    alignment=ft.alignment.center,
                )
            ]
        )
    )
    async def infinite_rotate():
        while True:
            animate_border.current.rotate.angle += math.radians(320)
            animate_border.current.update()
            await sleep(3)
    page.add(snake_border)
    page.run_task(infinite_rotate)
if __name__=="__main__":
    ft.app(target=main)