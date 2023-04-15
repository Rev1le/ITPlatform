CREATE MIGRATION m1pz2szd266cwfakmaushesy4c56lc4orz6gix7ay5kb72xcxhqw5a
    ONTO m1qdeyh3x7bsy3ritbrtobeqzzpmwwhzdk3nqhsdqinjudl3ezn4la
{
  ALTER TYPE default::Employer {
      DROP LINK recruiter;
  };
  ALTER TYPE default::Recruiter {
      DROP LINK vacancies;
  };
  ALTER TYPE default::Recruiter RENAME TO default::Mentor;
  ALTER TYPE default::Employer {
      CREATE LINK mentor := (.<employer[IS default::Mentor]);
      CREATE MULTI LINK vacancies -> default::Vacancy;
  };
  ALTER TYPE default::Mentor {
      CREATE REQUIRED PROPERTY resume -> std::str {
          SET REQUIRED USING ('');
      };
      CREATE REQUIRED PROPERTY salary -> std::float32 {
          SET REQUIRED USING (0.0);
      };
      CREATE REQUIRED PROPERTY skills -> array<std::str> {
          SET REQUIRED USING (<array<std::str>>[]);
      };
  };
};
