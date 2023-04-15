CREATE MIGRATION m1a4daap3hhylecysslfmaatynfknhnswioi5t3rkvhrw3c4s3qosq
    ONTO initial
{
  CREATE MODULE meta IF NOT EXISTS;
  CREATE FUTURE nonrecursive_access_policies;
  CREATE ABSTRACT TYPE meta::Created {
      CREATE REQUIRED PROPERTY created_at -> std::datetime {
          SET default := (std::datetime_current());
          SET readonly := true;
      };
  };
  CREATE ABSTRACT TYPE meta::Person EXTENDING meta::Created {
      CREATE PROPERTY bio -> std::str;
      CREATE REQUIRED PROPERTY birthday -> std::datetime;
      CREATE REQUIRED PROPERTY email -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE REQUIRED PROPERTY hash -> std::str;
      CREATE REQUIRED PROPERTY name -> std::str {
          CREATE CONSTRAINT std::max_len_value(1024);
      };
      CREATE PROPERTY photo -> std::str;
  };
  CREATE TYPE default::Employer EXTENDING meta::Person;
  CREATE TYPE default::Mentor EXTENDING meta::Created {
      CREATE REQUIRED LINK employer -> default::Employer;
      CREATE REQUIRED PROPERTY resume -> std::str;
      CREATE REQUIRED PROPERTY salary -> std::float32;
      CREATE REQUIRED PROPERTY skills -> array<std::str>;
  };
  ALTER TYPE default::Employer {
      CREATE LINK mentor := (.<employer[IS default::Mentor]);
  };
  CREATE TYPE default::Token EXTENDING meta::Created {
      CREATE REQUIRED LINK owner -> meta::Person;
      CREATE REQUIRED PROPERTY value -> std::str;
  };
  ALTER TYPE meta::Person {
      CREATE MULTI LINK tokens := (.<owner[IS default::Token]);
  };
  CREATE TYPE default::TaskCodeTest EXTENDING meta::Created {
      CREATE REQUIRED PROPERTY input -> std::str;
      CREATE REQUIRED PROPERTY output -> std::str;
  };
  CREATE ABSTRACT TYPE meta::Task EXTENDING meta::Created;
  CREATE TYPE default::TaskCode EXTENDING meta::Task {
      CREATE MULTI LINK tests -> default::TaskCodeTest;
      CREATE REQUIRED PROPERTY question -> std::str;
  };
  CREATE TYPE default::TaskQuestion EXTENDING meta::Task {
      CREATE REQUIRED PROPERTY answers -> array<std::str>;
      CREATE REQUIRED PROPERTY question -> std::str;
      CREATE REQUIRED PROPERTY right_answer -> std::str;
  };
  CREATE TYPE default::Vacancy EXTENDING meta::Created {
      CREATE REQUIRED LINK author -> default::Employer;
      CREATE REQUIRED PROPERTY about -> std::str;
      CREATE REQUIRED PROPERTY company -> std::str;
      CREATE REQUIRED PROPERTY name -> std::str;
      CREATE PROPERTY salary -> std::float32;
      CREATE REQUIRED PROPERTY skills -> array<std::str>;
  };
  ALTER TYPE default::Employer {
      CREATE MULTI LINK vacancies -> default::Vacancy;
  };
  CREATE TYPE default::TaskBlock EXTENDING meta::Created {
      CREATE MULTI LINK codes -> default::TaskCode;
      CREATE MULTI LINK questions -> default::TaskQuestion;
      CREATE REQUIRED PROPERTY description -> std::str;
      CREATE REQUIRED PROPERTY difficulty -> std::int16;
      CREATE REQUIRED PROPERTY name -> std::str;
  };
  CREATE TYPE default::Worker EXTENDING meta::Person {
      CREATE PROPERTY resume -> std::str;
      CREATE PROPERTY skills -> array<std::str>;
  };
  ALTER TYPE default::TaskBlock {
      CREATE MULTI LINK completed -> default::Worker;
      CREATE MULTI LINK failed -> default::Worker;
  };
  ALTER TYPE default::Worker {
      CREATE MULTI LINK completed := (.<completed[IS default::TaskBlock]);
  };
  ALTER TYPE default::Vacancy {
      CREATE MULTI LINK required_task_blocks -> default::TaskBlock;
  };
};
