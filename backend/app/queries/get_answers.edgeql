select TaskBlock {
    questions := .questions {
        id,
        question,
        answers,
        right_answer
    },
    codes := .codes {
        id,
        question,
        tests: {
            input,
            output
        }
    }
}
filter .id = <uuid>$task_block_id