CREATE MIGRATION m1gqs6q376ufcs7cluphdr2h3cosolpstveaj5rxacizhtgmp5fj4a
    ONTO m1vu6x7pjg7utogop76iasiqzn67x5mlmljfugf2uvt3yvhdjxkruq
{
  CREATE TYPE default::Vacancy EXTENDING meta::Created {
      CREATE REQUIRED PROPERTY about -> std::str;
      CREATE REQUIRED PROPERTY company -> std::str;
      CREATE REQUIRED PROPERTY name -> std::str;
      CREATE PROPERTY salary -> std::float32;
      CREATE REQUIRED PROPERTY skills -> array<std::str>;
  };
  CREATE TYPE default::Recruiter EXTENDING meta::Created {
      CREATE REQUIRED LINK employer -> default::Employer;
      CREATE MULTI LINK vacancies -> default::Vacancy;
  };
  ALTER TYPE default::Employer {
      CREATE LINK recruiter := (.<employer[IS default::Recruiter]);
  };
  CREATE ABSTRACT TYPE default::Task {
      CREATE PROPERTY about -> std::str;
  };
  CREATE TYPE default::TaskOne EXTENDING default::Task {
      CREATE PROPERTY lol -> std::str;
  };
  CREATE TYPE default::TaskTwo EXTENDING default::Task {
      CREATE PROPERTY kek -> std::str;
  };
  CREATE TYPE default::TaskBlock {
      CREATE MULTI LINK tasks -> default::Task;
  };
};
