insert Vacancy {
    author := (select Employer filter .id = <uuid>$employer_id),
    name := <str>$name,
    description := <str>$about,
    skills := <array<str>>$skills,
    company := <str>$company,
    salary := <optional str>$salary,
    required_task_blocks := distinct (for x in array_unpack(<array<uuid>>$required_task_block_ids) union (
       select TaskBlock
       filter .id = <uuid>x
       limit 1
    ))
}