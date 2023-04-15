select Mentor {
    name := .employer.name,
    bio := .employer.bio,
    photo := .employer.photo,
    skills,
    salary,
    resume
}