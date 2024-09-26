import logging
from datetime import datetime as dt

import click

from src.pipelines.inference import {{cookiecutter.project_python_slug}}_pipeline


@click.command(
    help="""
{{cookiecutter.project_name}} CLI {{cookiecutter.project_version}}.

Run the {{cookiecutter.project_name}} pipeline with various
options.

Examples:


  \b
  # Run the pipeline with default options
  python run.py
               
  \b
  # Run the pipeline without cache
  python run.py --no-cache


"""
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Disable caching for the pipeline run.",
)
def main(
    no_cache: bool = False,
):
    """Main entry point for the pipeline execution.

    This entrypoint is where everything comes together:

      * configuring pipeline with the required parameters
        (some of which may come from command line arguments)
      * launching the pipeline

    Args:
        no_cache: If `True` cache will be disabled.
    """

    # Run a pipeline with the required parameters. This executes
    # all steps in the pipeline in the correct order using the orchestrator
    # stack component that is configured in your active ZenML stack.
    pipeline_args = {}
    if no_cache:
        pipeline_args["enable_cache"] = False

    # Execute Pipeline

    run_pipeline = {{cookiecutter.project_python_slug}}_pipeline.with_options(
        config_path="config.yaml"
    ).with_options(**pipeline_args)
    run_pipeline()
    logging.info("Pipeline finished successfully!")


if __name__ == "__main__":
    main()
