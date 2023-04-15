update Employer
filter .id = <uuid>$id
set {
    bio := <optional str>$bio ?? .bio,
    photo := <optional str>$photo ?? .photo
}