from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from urllib.request import urlretrieve

with Diagram("Environments", show=False, filename="custom_remote", direction="LR", outformat='png'):

  # download the icon image files

    sf_url = "https://raw.githubusercontent.com/mohan-chinnappan-n5/dwg-icons/main/sf/sf.svg.png"
    sf_icon = "sf.svg.png"
    urlretrieve(sf_url, sf_icon)
    sf_st = Custom("ST", sf_icon)
    sf_sit = Custom("SIT", sf_icon)
    sf_uat = Custom("UAT", sf_icon)
    sf_staging = Custom("Staging", sf_icon)
    sf_PROD = Custom("Production", sf_icon)


    mulesoft_url = "https://raw.githubusercontent.com/mohan-chinnappan-n5/dwg-icons/main/sf/mulesoft.svg.png"
    mulesoft_icon = "mulesoft.svg.png"
    urlretrieve(mulesoft_url, mulesoft_icon)
    dev_int = Custom("DEV_INT", mulesoft_icon)
    QA_int = Custom("QA_INT", mulesoft_icon)
    PROD_int = Custom("PROD_INT", mulesoft_icon)

