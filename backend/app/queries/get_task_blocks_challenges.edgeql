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