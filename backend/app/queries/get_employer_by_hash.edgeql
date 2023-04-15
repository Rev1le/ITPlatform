select Employer {id, name, photo, birthday, bio, hash, email}
filter Employer.hash = <str>$hash
limit 1