# About

This is a demonstration vscode workspace for `vscode-python` issue [#2752](https://github.com/Microsoft/vscode-python/issues/2752)

It consists of a workspace containing two folders.  These folders are pretty much identical implementations of 
a simple microservice using the [nameko](https://www.nameko.io) framework.

## The Issue

The workspace configuration contains a compound launch configuration to launch both services when a debug session is started.

This will work **once**.  After stopping the debug session (by clicking the `stop` button in the debug bar to close
each service), subsequent debug sessions will fail.  One service will start, but the other will not, leading to a `timeout waiting for debugger` message.

## Steps to Reproduce

0. Ensure a `rabbitmq` server is available.  By default, the code will connect to `guest:guest@localhost`.  
1. Clone this repo
2. Create a `venv` in each service folder
3. Activate each virtual environment in turn, running `pip install -r requirements.txt` in each.
4. Open the `vscode-python-issue_2752.code-workspace` file to launch vscode.
5. Press `F5` and note that both services start fine.
6. Stop both running services
7. Press `F5` again.  Note that the launch of one service fails and leads to a `timeout waiting for debugger` message.
8. Press `Ctrl+Shift+P` and choose `Reload Window`
9. Press `F5` again.  The launch of both services now succeeds.


For reference, this is an example of Python Debug Console output for a 'good' launch:

```
Microsoft Windows [Version 10.0.17134.285]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\chris.platts\Source\Github\vscode-python-issue_2752\service_b>cd C:\Users\chris.platts\Source\Github\vscode-python-issue_2752\service_b && cmd /C "set "RABBITMQ_HOST=localhost" && set "PYTHONIOENCODING=UTF-8" && set "PYTHONUNBUFFERED=1" && set "GEVENT_SUPPORT=True" && set "PYTHONPATH=c:\Users\chris.platts\.vscode-insiders\extensions\ms-python.python-2018.8.0\pythonFiles\experimental\ptvsd" && C:\Users\chris.platts\Source\Github\vscode-python-issue_2752\service_b\env\Scripts\python.exe -m ptvsd --host localhost --port 58144 C:\Users\chris.platts\Source\Github\vscode-python-issue_2752\service_b\..\runner.py run service "
Runner: RABBITMQ_HOST=localhost
starting services: service_b
Connected to amqp://guest:**@127.0.0.1:5672//
```

## Notes

I've been using something of a workaround to get `nameko` services debuggable in vscode.  The 'official' way to launch a `nameko` service is either via code (via a call to `nameko.cli.main:main()`) or the command-line.

The `nameko` distribution provides an executable at `<env>\Scripts\nameko.exe` on Windows (or `<env>\bin\nameko` on osx/linux).

On osx/linux, the `nameko` command is a shebang'd python script, so it can be used in the `program` parameter of the launch configuration.

But, on windows, the `nameko` command is a binary executable, thus cannot be used in the same way.  To work around this, the launch configurations reference a `runner.py` script I wrote to take the same command-line args as the nameko cli tool and wrap the `nameko.cli.main:main()` call.

