select Employer {id, name, photo, birthday, bio, hash, email}
filter .hash = <str>$hash and .email = <str>$email
limit 1