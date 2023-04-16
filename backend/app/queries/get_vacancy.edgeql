select Vacancy {
    name,
    description,
    skills,
    company,
    salary,
    author_id := .author.id,
    required_task_blocks: {
        id,
        name,
        difficulty,
        description,
        is_completed := (select <uuid>$user_id in TaskBlock.completed.id),
        is_failed := (select <uuid>$user_id in TaskBlock.failed.id)
    }
}
filter .id = <uuid>$vacancy_id