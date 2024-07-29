#!/usr/bin/env bash
# Print build info to copy into `build.json` (a static file)

set -Eeuxo pipefail

echo '{"sha": "'$(git rev-parse HEAD || echo '')'"}'
