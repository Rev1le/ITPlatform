/*
CREATED BY: Rev1le <r.nikiy@yandex.ru>
CREATED ON: 06.05.2023
SECRIPTION: Query select one vacancy by uuid
*/

SELECT
	*,
	(
		SELECT GROUP_CONCAT(skill.name, ", ")
		FROM skill
		LEFT JOIN vacancy_skill
			ON vacancy_skill.skill_uuid == skill.uuid
		WHERE vacancy_skill.vacancy_uuid == vacancy.uuid
	) AS skills
FROM vacancy
WHERE vacancy.uuid=:uuid


 