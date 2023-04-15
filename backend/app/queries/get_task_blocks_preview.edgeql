select TaskBlock {
    name,
    difficulty,
    description,
    completed_count := count(.completed)
}