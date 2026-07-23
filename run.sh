#!/bin/bash

set -x -e -o pipefail
cd "$(dirname "$0")"

uv run \
  streamlit run \
  --server.headless True \
  --server.address 127.0.0.1 \
  --server.port 16666 \
  --logger.level debug \
  "$@"
