CREATE MIGRATION m1wfn5kj2m3l3ehdsxugbwi54rt6pmwsgopqt5djkfl7an23kkbyfa
    ONTO m1z4ia23dgxfnyjccjife6kp6wnam4qm6geurpf7nttl7zhrdzmk3q
{
  DROP TYPE default::Employer;
  ALTER TYPE default::Worker {
      ALTER PROPERTY resume {
          RESET OPTIONALITY;
      };
  };
  ALTER TYPE default::Worker {
      ALTER PROPERTY skills {
          RESET OPTIONALITY;
      };
  };
};
