select TaskBlock {
    questions := .questions {
        id,
        question,
        answers
    },
    codes := .codes {
        id,
        question
    }
}
filter .id = <uuid>$task_block_id