import os
import sys

# The following code is a workaround for the ModuleNotFoundError.
# for module_path in sys.path:
#     if module_path.endswith('opentelemetry_semantic_conventions'):
#         init_path = f'{module_path}/site-packages/opentelemetry/semconv/__init__.py'
#         if os.path.exists(init_path):
#             os.remove(init_path)

from traceloop import sdk
