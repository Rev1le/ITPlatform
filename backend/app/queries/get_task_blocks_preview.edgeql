select TaskBlock {
    id,
    name,
    difficulty,
    description,
    completed_count := count(.completed),
    completed := select <uuid>$user_id in TaskBlock.completed.id,
    failed := select <uuid>$user_id in TaskBlock.failed.id
}