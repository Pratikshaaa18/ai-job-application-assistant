from job_analyzer import analyze_job
from resume_suggester import suggest_resume_improvements
from cover_letter_generator import generate_cover_letter


def get_multiline_input(prompt_text: str) -> str:
    print(prompt_text)
    print("(Paste text. Press ENTER twice to finish)\n")

    lines = []
    empty_count = 0

    while True:
        line = input()

        if line.strip() == "":
            empty_count += 1
            if empty_count == 2:
                break
        else:
            empty_count = 0

        lines.append(line)

    return "\n".join(lines).strip()


if __name__ == "__main__":

    # 🔹 Dynamic Job Description
    job_description = get_multiline_input(
        "Enter Job Description:"
    )

    # 🔹 Dynamic Resume
    resume_text = get_multiline_input(
        "Enter Your Resume:"
    )

    # 🔹 Feature 1: Job Analysis
    job_details = analyze_job(job_description)
    print("\n📌 JOB DETAILS:\n", job_details)

    # 🔹 Feature 2: Resume Suggestions
    resume_suggestions = suggest_resume_improvements(
        job_details=str(job_details),
        resume_text=resume_text
    )
    print("\n📌 RESUME SUGGESTIONS:\n", resume_suggestions)

    # 🔹 Feature 3: Cover Letter
    cover_letter = generate_cover_letter(
        job_details=str(job_details),
        resume_text=resume_text
    )
    print("\n📌 COVER LETTER:\n")
    print(cover_letter)
