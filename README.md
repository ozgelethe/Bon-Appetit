    # Bon Appétit

    #### Video Demo:  <URL HERE>

    #### Description:
    The final project is a program that recommends random recipe based on the ingredients you had. The recipes are coming from a JSON file(https://frosch.cosy.sbg.ac.at/datasets/json/recipes/-/blob/main/recipes.json). You enter at least 3 material and the program cheks the JSON file and return you a recipe.

    <h1 align='center'><b>How To Run</b></h1>
    In terminal write "python project.py" to run project and "pytest project.py" to run test code.

    ### Requirements:
    to run this project you need pytest, sys, json

    ## Basics :
    The `main()` function is located in **project.py** file as well as other functions. They are nested on the same indentation level as main function.

    get_int function gets the materials that users had as an input.

    fullRecipies function gets recipes from json file.

    search_recipes function obviously searchs the all recipes in the json file, and finds matched recipes.

    recipe_times function calculates the which recipe has the most many matched ingredients.

    check_multiples function checks is there any recipe that added multiple times.

    show_recipe function asks the user that wanting to see recipe.

    If the answer is "yes" prints the recipe and Bon Appétit.

    Required `pip`-installable libraries are listed in `requirements.txt`.

    ## The manual
    1. Open the terminal emulator (Terminal, Windows Console etc.).
    2. `cd` to `project` directory.
    3. Type the following:
    ```
    python project.py
    ```
    4. Type a space after typing `python project.py` you can start playing by giving one only one character.
    5. Confirm by "enter" key.

    ## What files are included:
    - project.py,
    - test_project.py,
    - requirements.txt,
    - recipes.json,
    - README.md.