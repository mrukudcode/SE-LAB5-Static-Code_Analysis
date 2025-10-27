### Issue Table

| Issue                          | Type        | Line(s) | Description                                               | Fix Approach                                                  |
|-------------------------------|-------------|---------|-----------------------------------------------------------|---------------------------------------------------------------|
| Mutable default argument       | Bug         | 10      | `logs=[]` shared across calls                             | Changed to `logs=None` and initialized inside the function    |
| Bare except                    | Bug         | 25      | `except:` used without specifying exception type          | Replaced with `except (KeyError, ValueError)`                |
| Use of `eval()`               | Security    | 59      | `eval()` executes arbitrary code                          | Removed `eval()` entirely                                     |
| Unused import                  | Style       | 2       | `import logging` was unused                               | Logging now used for warnings and errors                     |
| Missing input validation       | Security    | 10, 25  | No type or value checks for `item` and `qty`              | Added `isinstance()` and `qty > 0` checks                    |
| File handling without `with`  | Style/Safety| 45, 50  | `open()` used without context manager                     | Replaced with `with open(...) as f:` and added encoding      |
| Naming convention violation    | Convention  | All     | Function names not in `snake_case`                        | Renamed to `add_item`, `remove_item`, etc.                   |
| String formatting              | Style       | 20      | Used `%` formatting instead of f-strings                  | Replaced with f-strings or lazy logging formatting           |
| Logging f-string interpolation| Style       | 15, 18, 37, 50, 58 | Used f-strings inside logging calls                        | Replaced with lazy `%` formatting in logging                 |
| Missing final newline          | Style       | 95      | No newline at end of file                                 | Added a blank line at the end                                |
| Function spacing               | Style       | Multiple| Expected 2 blank lines between functions                  | Added appropriate spacing between all function definitions   |
| Use of `global`               | Style       | 49      | `global stock_data` used                                  | Refactored to use `stock_data.clear()` and `update()`        |

