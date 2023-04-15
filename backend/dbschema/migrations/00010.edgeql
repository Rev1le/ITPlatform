CREATE MIGRATION m15ly3jtytdtspdo5zv65lmydz6eyi5ekioo4wka63dain5sgmrxyq
    ONTO m1gqs6q376ufcs7cluphdr2h3cosolpstveaj5rxacizhtgmp5fj4a
{
  ALTER TYPE default::Task {
      DROP PROPERTY about;
  };
  DROP TYPE default::TaskBlock;
  DROP TYPE default::TaskOne;
  DROP TYPE default::TaskTwo;
  DROP TYPE default::Task;
};
