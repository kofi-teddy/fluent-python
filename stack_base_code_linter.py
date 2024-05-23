from typing import Union


class Linter:
    def __init__(self):
        self.stack = []

    def lint(self, text: str) -> Union[bool, str]:
        """
        Lints the given text for matching opening and closing braces.

        Args:
            text (str): The text to be linted.

        Returns:
            Union[bool, str]: True if the text has balanced braces, otherwise an error message.

        """
        for char in text:
            if self.is_opening_brace(char):
                self.stack.append(char)
            elif self.is_closing_brace(char):
                popped_opening_brace = self.stack.pop()
                if not popped_opening_brace:
                    return f"{char} doesn't have opening brace"
                if self.is_not_a_match(popped_opening_brace, char):
                    return f"{char} has mismatched opening brace"

        if self.stack:
            return f"{self.stack[-1]} does not have closing brace"

        return True

    def is_opening_brace(self, char: str) -> bool:
        """
        Checks if the given character is an opening brace.

        Args:
            char (str): The character to be checked.

        Returns:
            bool: True if the character is an opening brace, False otherwise.

        """
        return char in ["(", "[", "{"]

    def is_closing_brace(self, char: str) -> bool:
        """
        Checks if the given character is a closing brace.

        Args:
            char (str): The character to be checked.

        Returns:
            bool: True if the character is a closing brace, False otherwise.

        """
        return char in [")", "]", "}"]

    def is_not_a_match(self, opening_brace: str, closing_brace: str) -> bool:
        """
        Checks if the given opening and closing braces are a mismatched pair.

        Args:
            opening_brace (str): The opening brace character.
            closing_brace (str): The closing brace character.

        Returns:
            bool: True if the braces are mismatched, False otherwise.

        """
        return closing_brace != {"(": ")", "[": "]", "{": "}"}[opening_brace]


linter = Linter()
print(linter.lint("( var x = { y: [1, 2, 3] } )"))