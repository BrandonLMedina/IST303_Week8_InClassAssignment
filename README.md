# IST303_Week8_InClassAssignment
In class team exercise repo for IST 303 Software Development.


# Team Johto – Team Exercise 2

This document summarizes the issues identified in the original `team_ex_2.py` codebase and the tasks, assignments, and solutions proposed by Team Johto.

---

## Issues

1. **Hardcoded search term without user input**  
2. **No dedicated output directory**  
3. **Duplicated logic**  
4. **File name built from page titles** (may contain invalid characters)  
5. **No error handling in the code**  
6. **No timing and performance measurement**  
7. **No result size limit**

---

## Tasks, Assignments, and Solutions

| Task # | Task                         | Description                                                                                                   | Assignment       | Solution                                                                                                                                                            |
|--------|------------------------------|---------------------------------------------------------------------------------------------------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | Add user input               | Every function uses the same search term                                                                      | Alex_Corona      | Call the variable `term = input()` and have the search term passed into `get_search_results`.                                                                      |
| 2      | Create output directory      | The code has no dedicated output directory, which means the output would be placed in the same directory as the code | Haoran_Jin       | Create a function `ensure_output_dir()` that makes a folder named `wiki_dl` and redirect all `.txt` output files into that folder.                                |
| 3      | Remove duplicate logic       | The download-and-save logic is repeated in multiple functions and creates unnecessary duplication             | Alex Corona      | Combine all repeated logic into one reusable function `dl_and_save()` so that sequential, thread, and process functions all call the same code.                   |
| 4      | Use Regex to create filenames| File name is generated from page title which can contain invalid characters                                   | Brandon Medina   | Import and add `re` to `out_filename` to remove illegal characters.                                                                                                |
| 5      | Add error handling           | The code has no error handling, which can cause crashes when pages fail to load or files fail to write       | Haoran_Jin       | Add `try/except` blocks around `wikipedia.page()` and file writing to catch exceptions and print informative error messages without stopping the program.         |
| 6      | Add timing wrapper           | There is no way to compare the performance of sequential, threaded, and process methods                      | Brandon Medina   | Create a simple timing decorator `@timeit` that prints how long each execution method takes, allowing the team to compare performance.                            |
| 7      | Add result return limits     | The current code does not specify the number of pages to return, which allows for the possibility of retrieving too many pages | Brandon Medina   | Add a limit to `results = wikipedia.search(...)`.                                                                                                                  |

---
