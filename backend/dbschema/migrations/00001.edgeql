CREATE MIGRATION m13m54giksuaz2thsst723muqs62732meyy4efszfmp64nhj24j2lq
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
      CREATE REQUIRED PROPERTY bio -> std::str;
      CREATE REQUIRED PROPERTY birthday -> std::datetime;
      CREATE REQUIRED PROPERTY hash -> std::str;
      CREATE REQUIRED PROPERTY name -> std::str {
          CREATE CONSTRAINT std::max_len_value(1024);
      };
      CREATE REQUIRED PROPERTY photo -> std::str;
  };
  CREATE TYPE default::Token EXTENDING meta::Created {
      CREATE REQUIRED LINK owner -> meta::Person;
      CREATE REQUIRED PROPERTY value -> std::str;
  };
  CREATE TYPE default::Worker EXTENDING meta::Person {
      CREATE REQUIRED PROPERTY resume -> std::str;
      CREATE REQUIRED PROPERTY skills -> array<std::str>;
  };
  CREATE ABSTRACT TYPE meta::Employer EXTENDING meta::Person;
};
