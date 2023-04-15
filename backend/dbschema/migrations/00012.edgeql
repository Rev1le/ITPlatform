CREATE MIGRATION m1qdeyh3x7bsy3ritbrtobeqzzpmwwhzdk3nqhsdqinjudl3ezn4la
    ONTO m1fopuqrqgot7hmowzvyjexrpju7jrztaxrzfkbfjpe5ok3jd5tiba
{
  ALTER TYPE default::Worker {
      CREATE MULTI LINK completed := (.<completed[IS default::TaskBlock]);
  };
};
