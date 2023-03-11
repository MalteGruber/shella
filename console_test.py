import shella
import asyncio

counter = 0

@shella.shell_cmd(["show", "s"], desc="Show counter state")
async def show(args):
    print(f"counter={counter}")

@shella.shell_cmd("set", desc="Set counter state", template="%s", usage="[count]")
async def test(args):
    if len(args) != 2:
        print("Please provide a number")
    global counter
    counter = int(args[1])


async def my_task():
    global counter

    while shella.is_running():
        await asyncio.sleep(1)
        counter += 1
        shella.set_prompt(f"demo{counter:03d}$")


async def main():
    shella_task_ = asyncio.create_task(shella.shell_task())
    my_task_ = asyncio.create_task(my_task())
    shella.set_prompt(f"demo{counter:03d}$")
    await shella_task_
    await my_task_
    print("Good bye!")

asyncio.run(main())