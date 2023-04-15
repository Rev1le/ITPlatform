CREATE MIGRATION m1fopuqrqgot7hmowzvyjexrpju7jrztaxrzfkbfjpe5ok3jd5tiba
    ONTO m15ly3jtytdtspdo5zv65lmydz6eyi5ekioo4wka63dain5sgmrxyq
{
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
  CREATE TYPE default::TaskBlock EXTENDING meta::Created {
      CREATE MULTI LINK codes -> default::TaskCode;
      CREATE MULTI LINK completed -> default::Worker;
      CREATE MULTI LINK questions -> default::TaskQuestion;
      CREATE REQUIRED PROPERTY description -> std::str;
      CREATE REQUIRED PROPERTY difficulty -> std::int16;
      CREATE REQUIRED PROPERTY name -> std::str;
  };
};
