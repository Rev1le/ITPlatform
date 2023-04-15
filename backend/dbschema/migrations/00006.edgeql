CREATE MIGRATION m1z4ia23dgxfnyjccjife6kp6wnam4qm6geurpf7nttl7zhrdzmk3q
    ONTO m13l6fo2tohpjubrhr5roy3izuexugvko6u6rk2nv3xeoaifiphyda
{
  ALTER TYPE meta::Person {
      ALTER PROPERTY bio {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE meta::Person {
      ALTER PROPERTY photo {
          RESET OPTIONALITY;
      };
  };
};
