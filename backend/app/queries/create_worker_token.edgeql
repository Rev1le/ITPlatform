insert Token {
    value := <str>$token,
    owner := (
        select Worker
        filter .id = <uuid>$user_id
    )
}