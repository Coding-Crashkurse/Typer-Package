import typer

app = typer.Typer()


# @app.command()
# # def hallo(name: str, formell: bool):
# def hallo(name: str, formell: bool = False):
#     if formell:
#         typer.echo(f"Guten Tag Herr {name}")
#     else:
#         typer.echo(f"Hallo {name}")

@app.command()
def hi(name: str):
    typer.echo(f"Hallo {name}")



@app.command()
# def hallo(name: str, formell: bool):
def hallo(
    name: str = typer.Option(..., help="Name, den man ansprechen will"),
    formell: bool = typer.Option(False, help="Formelle Ansprache, ja oder nein"),
):
    if formell:
        typer.echo(f"Guten Tag Herr {name}")
    else:
        typer.echo(f"Hallo {name}")

