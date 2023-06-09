# Shella

Shella is a Python module that enables you to interact with your python script using a command line. Provided commands run asynchronously as async functions.  In addition to its asynchronous functionality, Shella also provides autocompleting, history, and argument validation features. 

Autocompleting enables users to save time by automatically completing commands as they type. History allows users to recall previous commands and reuse them easily. Argument validation ensures that commands are executed with the correct arguments, minimizing errors and increasing efficiency.

## How to try
Use Linux (Windows is currently not supported!) and run
```python
pip3 install shella
```
Here is an example program to you started
```python
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
```


## Declaring commands
Commands are declared using the function decorator `@shella.shell_cmd(commands,..)` which turns a function into a callable. The function must have one argument to which a list of the arguments are passed.



`commands` a string or list of at most two strings representing the command.

#### Options
The following arguments can be provided to the function decorator to modify the behaviour of the command:

- `desc`: a string with a description, shown in the help list

- `template` a string containing a template to match the provided arguments to, availible types are 
String: `%s`, Integer: `%d`, and float: `%f`

- `usage`: String to provide information about the usage of the command, shown on error or arguments that do not match the template

#### Example
```python
@shella.shell_cmd("foo",template="%d %s")
def set(argv):
    print(argv)
#calling the command as "foo 123 bar" results in print() printing
#["foo",123,"bar"]

```

## Setting the prompt

The prompt can be set at any time using the prompt updates live, which means that it can be dynamically changed during the usage of the program.

```python
shella.set_prompt("shella$")
```