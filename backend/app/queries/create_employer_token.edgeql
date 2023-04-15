insert Token {
    value := <str>$token,
    owner := (
        select Employer
        filter .id = <uuid>$user_id
    )
}