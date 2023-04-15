select Worker {id, name, photo}
filter Worker.hash = <str>$hash
limit 1