select TaskBlock {
    id,
    name,
    difficulty,
    description,
    completed_count := count(.completed),
    is_completed := (select <uuid>$user_id in TaskBlock.completed.id),
    is_failed := (select <uuid>$user_id in TaskBlock.failed.id)
}