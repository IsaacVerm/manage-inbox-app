import click
import os

@click.group()
def cli():
    pass

@cli.command()
@click.argument('file')
def clns(file):
    """Count total number of lines in markdown file"""
    try:
        # Check if file exists and has .md extension
        if not os.path.exists(file):
            click.echo(f"Error: File '{file}' not found.")
            return
        if not file.endswith('.md'):
            click.echo(f"Error: File '{file}' is not a markdown file.")
            return

        # Read the file and count lines
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            total_lines = len(lines)
            
            # Remove empty lines from count
            # line.strip() returns an empty string '' if line is empty
            # empty strings are considered falsy values in Python
            # you can check this yourself by comparing bool('') and bool('some string')
            non_empty_lines = len([line for line in lines if line.strip()])
            
            # Output results
            click.echo(f"Total lines: {total_lines}")
            click.echo(f"Non-empty lines: {non_empty_lines}")
            click.echo(f"Empty lines: {total_lines - non_empty_lines}")

    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    cli()