/*
CREATED BY: Rev1le <r.nikiy@yandex.ru>
CREATED ON: 06.05.2023
SECRIPTION: Query gets all mentors with skills
*/
SELECT
    *,
	(
		SELECT
		    GROUP_CONCAT(skill.name, ", ")
		FROM skill
		LEFT JOIN mentor_skill
		    ON mentor_skill.skill_uuid == skill.uuid
		WHERE
		    mentor_skill.mentor_uuid == mentor.uuid
	) AS skills
FROM
    user, mentor
WHERE
    user.uuid = mentor.uuid