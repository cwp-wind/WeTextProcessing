#!/bin/bash
PYTHONPATH=$(cd "$(dirname $0)" && pwd):$PYTHONPATH

# 运行全部
# pytest normalizer_test.py

# 运行特定case
pytest normalizer_test.py::TestNormalizer
