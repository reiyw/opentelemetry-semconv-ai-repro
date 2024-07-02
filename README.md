# Reproduction of the `ModuleNotFoundError` in the `opentelemetry-semantic-conventions-ai` package

1. [Install Bazel](https://bazel.build/install).
2. Run `bazel run :main`. The following error is output.

```
Traceback (most recent call last):
  File "/home/ryo.takahashi/.cache/bazel/_bazel_ryo.takahashi/73da590b5d6f7b4220b10a2aad9d98d9/execroot/_main/bazel-out/k8-fastbuild/bin/main.runfiles/_main/main.py", line 11, in <module>
    from traceloop import sdk
  File "/home/ryo.takahashi/.cache/bazel/_bazel_ryo.takahashi/73da590b5d6f7b4220b10a2aad9d98d9/execroot/_main/bazel-out/k8-fastbuild/bin/main.runfiles/rules_python~~pip~my_deps_311_traceloop_sdk/site-packages/traceloop/sdk/__init__.py", line 14, in <module>
    from traceloop.sdk.metrics.metrics import MetricsWrapper
  File "/home/ryo.takahashi/.cache/bazel/_bazel_ryo.takahashi/73da590b5d6f7b4220b10a2aad9d98d9/execroot/_main/bazel-out/k8-fastbuild/bin/main.runfiles/rules_python~~pip~my_deps_311_traceloop_sdk/site-packages/traceloop/sdk/metrics/metrics.py", line 10, in <module>
    from opentelemetry.semconv.ai import Meters
ModuleNotFoundError: No module named 'opentelemetry.semconv.ai'
```
