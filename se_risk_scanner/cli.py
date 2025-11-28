import sys
import click

from .loader import load_contract_sources
from .parser import parse_contracts
from .rules.runner import run_all_rules
from .scoring import score_contract
from .reporting import print_text_report, to_json_report


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--format", "fmt", type=click.Choice(["text", "json"]), default="text")
def main(path: str, fmt: str) -> None:
    """Scan Solidity contracts at PATH for economic risks."""
    sources = load_contract_sources(path)
    if not sources:
        click.echo("No Solidity sources found.", err=True)
        sys.exit(1)

    profiles = parse_contracts(sources)
    results = []
    for profile in profiles:
        findings = run_all_rules(profile)
        score = score_contract(findings)
        results.append((profile, findings, score))

    if fmt == "json":
        click.echo(to_json_report(results))
    else:
        print_text_report(results)


if __name__ == "__main__":
    main()
