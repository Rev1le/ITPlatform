select Worker {id, name, photo, birthday, bio, hash, email}
filter Worker.hash = <str>$hash
limit 1