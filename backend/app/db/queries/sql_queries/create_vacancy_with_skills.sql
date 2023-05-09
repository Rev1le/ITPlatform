/*
CREATED BY: Rev1le <r.nikiy@yandex.ru>
CREATED ON: 05.05.2023
SECRIPTION: Query creates a vacancy with links to skills
*/

insert into vacancy (uuid, name, description, salary, company, author_uuid) 
	VALUES (:uuid, :name, :description, :salary, :company, :author_uuid); 

insert into vacancy_skill
	SELECT :uuid, skill.uuid from skill WHERE skill.name IN :skills;

 