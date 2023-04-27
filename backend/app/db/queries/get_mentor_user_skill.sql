SELECT 
	user.name, 
	user.birthday, 
	user.bio, 
	user.photo, 
	mentor.uuid,
	mentor.salary, 
	mentor.resume,
	(
		SELECT GROUP_CONCAT(skill.name, ", ") 
		FROM skill
		LEFT JOIN mentor_skill 
		ON mentor_skill.skill_uuid == skill.uuid
		WHERE mentor_skill.mentor_uuid == mentor.uuid
	) AS skills
FROM user, mentor
WHERE user.uuid = mentor.uuid AND user.uuid == :uuid