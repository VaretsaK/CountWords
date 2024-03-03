import re


def count_words(file_name: str) -> str:
    """
    This function reads a given file and returns amount of words in it.
    :param file_name:
    :return:
    """

    # opening file and saving its content in a variable
    with open(file_name, "r") as file:
        file_content = file.read()

    # making a list of words from a file's content
    list_of_words = re.findall(r"[a-zA-Z]+'?[a-zA-Z]*", file_content)

    return f"In this text {len(list_of_words)} word(s)"
