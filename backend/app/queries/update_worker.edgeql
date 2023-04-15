update Worker
filter .id = <uuid>$id
set {
    birthday := <optional datetime>$birthday ?? .birthday,
    hash := <optional str>$hash ?? .hash,
    email := <optional str>$email ?? .email,
    bio := <optional str>$bio ?? .bio,
    photo := <optional str>$photo ?? .photo,
    resume := <optional str>$resume ?? .resume,
    skills := <optional array<str>>$skills ?? .skills
}