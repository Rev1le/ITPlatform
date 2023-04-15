select TaskBlock {
    id,
    name,
    difficulty,
    description,
    completed_count := count(.completed)
}
filter .id = <uuid>$user_id