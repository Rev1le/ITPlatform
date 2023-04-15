CREATE MIGRATION m13l6fo2tohpjubrhr5roy3izuexugvko6u6rk2nv3xeoaifiphyda
    ONTO m1bfmwquio3nhyxo46j4dz7tyrs5vvpte7lvyhd5xjevnwkm64zuya
{
  ALTER TYPE meta::Person {
      CREATE MULTI LINK tokens := (.<owner[IS default::Token]);
  };
};
