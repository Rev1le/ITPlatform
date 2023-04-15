insert Mentor {
    employer := (
        select Employer
        filter .id = <uuid>$user_id
    ),
    skills := <array<str>>$skills,
    salary := <float32>$salary,
    resume := <str>$resume
}