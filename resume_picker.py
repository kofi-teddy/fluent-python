from typing import List


def pick_resume(resumes: List[str]) -> str:
    """
    Picks the most suitable resume from a list of resumes.

    Args:
        resumes: A list of resumes.

    Returns:
        The most suitable resume.

    Raises:
        ValueError: If the list of resumes is empty.
    """
    eliminate = "top"

    while len(resumes) > 1:
        if eliminate == "top":
            resumes = resumes[len(resumes) // 2: len(resumes) - 1]
            eliminate = "bottom"
        elif eliminate == "bottom":
            resumes = resumes[0: len(resumes) // 2]
            eliminate = "top"

    if len(resumes) == 0:
        raise ValueError("No resumes found.")

    return resumes[0]