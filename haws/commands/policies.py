import click
from haws.services.aws.policy_check import *

@click.command()
@click.pass_context
def cli(ctx):
    run_policy_check()