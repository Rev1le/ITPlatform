CREATE MIGRATION m1u7zpqhrtylbid7tmdkl25qaqoo4py7b6bop22aocbzrgiinea3oq
    ONTO m1pz2szd266cwfakmaushesy4c56lc4orz6gix7ay5kb72xcxhqw5a
{
  ALTER TYPE default::TaskBlock {
      CREATE MULTI LINK failed -> default::Worker;
  };
};
