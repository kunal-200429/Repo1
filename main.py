import typer
import subprocess
import sys
from pathlib import Path

app = typer.Typer()

@app.command()
def web():
    """Start the web interface"""
    print("Starting web server at http://127.0.0.1:5000/")
    print("Open your browser to http://127.0.0.1:5000/ for the web interface")
    from api import app
    app.run(host='127.0.0.1', port=5000, debug=True)

@app.command()
def cli():
    """Start the CLI interface"""
    from cli import app as cli_app
    cli_app()

if __name__ == "__main__":
    app()
