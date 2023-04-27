/*
CREATED BY: Rev1le <r.nikiy@yandex.ru>
CREATED ON: 27.04.2023
SECRIPTION: Queryt gets all mentors with data from the user table and skills from the skill table
*/
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
WHERE user.uuid = mentor.uuid