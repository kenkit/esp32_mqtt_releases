Yes, it is possible to include the `data` directory in the firmware. You can do this by using the `board_build.embed_files` option in your `platformio.ini` file.

This option allows you to specify a list of files or folders that will be converted into a binary blob and embedded into the firmware. You can then access this data from your code.

Here's an example of how you would use it in your `platformio.ini` file:

```ini
[env:esp8266]
platform = espressif8266
board = d1
...
board_build.embed_files = 
    data/ca_000.der
    data/ca_001.der
    ...
```

You would need to list all the files in the `data` directory that you want to include.

Alternatively, you can create a script to automatically generate the list of files and add it to the `platformio.ini` file.

Would you like me to modify the `platformio.ini` file to include the `data` directory?
