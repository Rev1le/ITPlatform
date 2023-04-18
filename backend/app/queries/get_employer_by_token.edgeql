select Employer {id, name, photo, birthday, bio, hash, email, mentor}
filter .tokens.value = <str>$token
limit 1