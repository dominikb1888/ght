import click
import os
from urllib.request import urlopen, Request
import json


@click.group()
@click.version_option()
def cli():
    "A set of github tools for managing groups"


@cli.command(name="command")
@click.argument(
    "ghorg"
)
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def gen_gallery(ghorg, option):
    "Creates a markdown image gallery from all users commiting to a group"

    ## TODO: Check if .env file exists if not ask user to create one
    ## TODO: authenticate via gh?
    config = {
        'GHTOKEN': os.environ.get("GHTOKEN"),
        'GHORG': os.environ.get("GHORG")
    }

    headers = {
         'Authorization': f"token {config['GHTOKEN']}",
         'Accept': 'application/vnd.github.v3+json'
    }

    url = f"https://api.github.com/orgs/{config['GHORG']}/repos?per_page=100"
    httprequest = Request(url, headers=headers)

    with urlopen(httprequest) as response:
        if response.status == 200:
            data = json.loads(response.read().decode())
            names = []
            for repo in data:
                names.append(repo['name'])
        else:
            click.echo(f"Failed to fetch repos. Status code: {response.status_code}")
            break

    authors = {}
    for name in names:
        # https://api.github.com/repos/23W-GBAC/SenaDok/commits
        click.echo(url)
        url = f"https://api.github.com/repos/23W-GBAC/{name}/commits"
        httprequest = Request(url, headers=headers)
        with urlopen(httprequest) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                author = data[0]['author']
                if author:
                    authors[author['login']] = author
            else:
                click.echo(f"Failed to fetch commits. Status code: {response.status_code}")
                break

    text = []
    for author in authors.values():
        name = author['login']
        img = author['avatar_url']
        text.append(f"[![{name}]({img})]({url})")

    result = " ".join(text)
    click.echo(result)

    with open('gallery.md', 'w') as file:
        file.write(result)
