CREATE MIGRATION m1ytjhhtxfi2xmwy6g6dpfsj6hfwdpaoefbpr4kwxr7t7yqf6uze2a
    ONTO m13m54giksuaz2thsst723muqs62732meyy4efszfmp64nhj24j2lq
{
  ALTER TYPE meta::Person {
      CREATE REQUIRED PROPERTY email -> std::str {
          SET REQUIRED USING ('');
      };
  };
};
