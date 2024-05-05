# lego-handlers

```py3
def do_something() -> None:
    cmd_result = asyncio.run(
        lego_handlers.run_and_collect_events(
            cmd=Command()
        )
    )
    return asyncio.run(
        lego_handlers.process_result(
            cmd_result=cmd_result,
            client_handler=client_handle,
            publish_events=True,
        )
    )

```