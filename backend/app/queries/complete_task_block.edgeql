update TaskBlock
filter .id = <uuid>$task_block_id
set {
    completed := distinct(.completed union (
        select Worker filter .id = <uuid>$user_id
    ))
}