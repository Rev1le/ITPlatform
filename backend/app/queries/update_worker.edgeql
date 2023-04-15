update Worker
filter .id = <uuid>$id
set {
    bio := <optional str>$bio ?? .bio,
    photo := <optional str>$photo ?? .photo,
    resume := <optional str>$resume ?? .resume,
    skills := <optional array<str>>$skills ?? .skills
}