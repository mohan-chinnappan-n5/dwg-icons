
import sf_st, sf_sit, sf_uat, sf_staging, sf_PROD, dev_int, QA_int, PROD_int  from remote_icons_sf


with Cluster("CRM"):
    sf_st >> sf_sit >> sf_sit >> sf_uat >> sf_staging >> sf_PROD
    sf_st >> dev_int
    sf_sit >> QA_int
    sf_uat >> QA_int 
    sf_staging >> QA_int  
    sf_PROD >> PROD_int
