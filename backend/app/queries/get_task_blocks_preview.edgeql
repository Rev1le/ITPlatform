select TaskBlock {
    id,
    name,
    difficulty,
    description,
    completed_count := count(.completed)
}