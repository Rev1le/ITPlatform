select Employer {id, name, photo, birthday, bio, hash, email}
filter .tokens.owner.id = <uuid>$user_id
limit 1