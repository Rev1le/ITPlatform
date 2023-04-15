CREATE MIGRATION m1qhec6yvnk6u27rinyh6kof4vah4jdddtwpmv4af5iu34q5r767pa
    ONTO m1ytjhhtxfi2xmwy6g6dpfsj6hfwdpaoefbpr4kwxr7t7yqf6uze2a
{
  CREATE TYPE default::Employer EXTENDING meta::Person;
  DROP TYPE meta::Employer;
};
