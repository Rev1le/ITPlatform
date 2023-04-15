insert Token {
    value := <str>$token,
    owner := (
        select meta::Person
        filter .id = <uuid>$user_id
    )
}