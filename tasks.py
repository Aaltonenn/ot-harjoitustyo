from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def start_tui(ctx):
    ctx.run("python3 src/index2.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest src", pty = True)

@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src", pty = True)
    ctx.run("coverage html", pty = True)

@task
def lint(ctx):
    ctx.run("pylint src")
