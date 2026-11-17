from phoenix.otel import register

from config.phoenix_config import (
    PHOENIX_AUTO_INSTRUMENT,
    PHOENIX_PROJECT_NAME,
)

# Register the Phoenix tracer for this project using settings from
# config/phoenix_config.py.
tracer_provider = register(
    project_name=PHOENIX_PROJECT_NAME,
    auto_instrument=PHOENIX_AUTO_INSTRUMENT,
)
