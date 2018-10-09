"""
This is a workaround for the fact that nameko on windows deploys a 'nameko.exe' under `<env>\Scripts\`

On windows, the `nameko` tool cannot be used as the value for "program" in launch.json, since items
is a binary executable.

On osx/linux, `<env>\bin\nameko' is a shell script, which vscode has no problem using as the 
value for the launch configuration's "program" parameter.

"""

import sys
import os

print("Runner: RABBITMQ_HOST={0}".format(os.environ.get("RABBITMQ_HOST")))

from nameko.cli.main import main
main()