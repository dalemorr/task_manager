# Task Manager

Run `python3 ./src/task_manager.py` to run the program with default input and output. By default, the program will use `stdin` as input and `./task_manager.db` as output.

To run from an input file, use `-f <input-file>`. To run with a different output, use `-o <output-file>`.

Input should be formatted for an SQLite query. Invalid SQLite will be rejected with an error message.

`.gitignore` is set to ignore `*.db` files and `*.sql` files by default. Do not upload any sensitive data to a public repository.