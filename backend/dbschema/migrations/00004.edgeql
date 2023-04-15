CREATE MIGRATION m1bfmwquio3nhyxo46j4dz7tyrs5vvpte7lvyhd5xjevnwkm64zuya
    ONTO m1qhec6yvnk6u27rinyh6kof4vah4jdddtwpmv4af5iu34q5r767pa
{
  ALTER TYPE meta::Person {
      ALTER PROPERTY email {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
