select Worker {id, name, photo, birthday, bio, hash, email}
filter .tokens.value = <str>$token
limit 1